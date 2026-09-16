from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field, ConfigDict


class Message(BaseModel):
    model_config = ConfigDict(extra="forbid")

    role: Literal["system", "user", "assistant"]
    content: str = Field(min_length=1, max_length=100_000)


class RequestMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid")

    session_id: str | None = Field(default=None, max_length=128)
    use_rag: bool = True
    rag_collection: str | None = Field(default=None, max_length=128)


class ChatCompletionRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    model: str = Field(min_length=1)
    messages: list[Message] = Field(min_length=1)
    stream: bool = False
    max_tokens: int = Field(default=512, ge=1, le=4096)
    temperature: float = Field(default=0.2, ge=0, le=2)
    top_p: float = Field(default=0.9, gt=0, le=1)
    metadata: RequestMetadata | None = None


class RagSource(BaseModel):
    document_id: str
    chunk_id: str
    title: str
    score: float
    url: str | None = None


class Usage(BaseModel):
    prompt_tokens: int = Field(ge=0)
    completion_tokens: int = Field(ge=0)
    total_tokens: int = Field(ge=0)


class ChatChoice(BaseModel):
    index: int = Field(ge=0)
    message: Message
    finish_reason: Literal["stop", "length", "safety", "error"]


class ChatCompletionResponse(BaseModel):
    id: str
    object: Literal["chat.completion"] = "chat.completion"
    created: int
    model: str
    choices: list[ChatChoice]
    usage: Usage
    rag_sources: list[RagSource] = Field(default_factory=list)


class ErrorDetail(BaseModel):
    code: str
    message: str
    request_id: str
    retryable: bool = False


class ErrorResponse(BaseModel):
    error: ErrorDetail


class HealthResponse(BaseModel):
    status: Literal["ok", "degraded"]
    version: str
