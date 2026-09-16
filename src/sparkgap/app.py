from __future__ import annotations

import time
import uuid
import json

from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.responses import JSONResponse, StreamingResponse

from . import __version__
from .config import Settings
from .events import emit_event
from .ingestion import load_index
from .model import ModelAdapter
from .models import ChatChoice, ChatCompletionRequest, ChatCompletionResponse, ErrorDetail, ErrorResponse, HealthResponse, Message, RagSource, Usage
from .retrieval import search
from .safety import classify_input, refusal

settings = Settings.from_env()
app = FastAPI(title="Project Sparkgap Inference API", version=__version__)


def _request_id(value: str | None) -> str:
    return value or f"req_{uuid.uuid4().hex}"


def _error(status: int, code: str, message: str, request_id: str, retryable: bool = False) -> JSONResponse:
    payload = ErrorResponse(error=ErrorDetail(code=code, message=message, request_id=request_id, retryable=retryable))
    return JSONResponse(status_code=status, content=payload.model_dump())


@app.get("/v1/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok", version=__version__)


@app.post("/v1/chat/completions", response_model=ChatCompletionResponse)
async def chat_completions(
    payload: ChatCompletionRequest,
    x_tenant_id: str | None = Header(default=None),
    x_request_id: str | None = Header(default=None),
) -> ChatCompletionResponse | JSONResponse | StreamingResponse:
    request_id = _request_id(x_request_id)
    if not x_tenant_id:
        return _error(400, "missing_tenant", "X-Tenant-ID is required.", request_id)
    question = next((message.content for message in reversed(payload.messages) if message.role == "user"), "")
    safety_reason = classify_input(question)
    emit_event("query_submitted", request_id, tenant_id=x_tenant_id, model=payload.model)
    if safety_reason:
        text = refusal(safety_reason)
        emit_event("safety_blocked", request_id, tenant_id=x_tenant_id, reason=safety_reason)
        return _response(payload.model, text, [], request_id, finish_reason="safety")

    chunks = load_index(settings.index_path)
    results = search(chunks, question) if (payload.metadata is None or payload.metadata.use_rag) else []
    adapter = ModelAdapter(settings)
    started = time.perf_counter()
    try:
        answer = await adapter.generate(question, results, payload.max_tokens, payload.temperature)
    except Exception as exc:
        emit_event("generation_failed", request_id, error=type(exc).__name__)
        return _error(502, "model_unavailable", "The configured model is unavailable.", request_id, retryable=True)
    emit_event("response_completed", request_id, tenant_id=x_tenant_id, latency_ms=round((time.perf_counter() - started) * 1000), source_count=len(results))
    sources = [RagSource(document_id=item.chunk.document_id, chunk_id=item.chunk.chunk_id, title=item.chunk.title, score=item.score, url=item.chunk.url) for item in results]
    response = _response(payload.model, answer.text, sources, request_id, answer.prompt_tokens, answer.completion_tokens)
    if payload.stream:
        return StreamingResponse(_sse(response), media_type="text/event-stream", headers={"X-Request-ID": request_id})
    return response


def _response(model: str, text: str, sources: list[RagSource], request_id: str, prompt_tokens: int = 0, completion_tokens: int | None = None, finish_reason: str = "stop") -> ChatCompletionResponse:
    completion_tokens = completion_tokens if completion_tokens is not None else len(text.split())
    return ChatCompletionResponse(
        id=f"chatcmpl_{request_id}",
        created=int(time.time()),
        model=model,
        choices=[ChatChoice(index=0, message=Message(role="assistant", content=text), finish_reason=finish_reason),],
        usage=Usage(prompt_tokens=prompt_tokens, completion_tokens=completion_tokens, total_tokens=prompt_tokens + completion_tokens),
        rag_sources=sources,
    )


def _sse(response: ChatCompletionResponse):
    content = response.choices[0].message.content
    event = {
        "id": response.id,
        "object": "chat.completion.chunk",
        "model": response.model,
        "choices": [{"index": 0, "delta": {"role": "assistant", "content": content}, "finish_reason": None}],
    }
    yield f"data: {json.dumps(event)}\n\n"
    yield "data: [DONE]\n\n"
