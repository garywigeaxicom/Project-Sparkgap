from __future__ import annotations

import re
from dataclasses import dataclass

import httpx

from .config import Settings
from .retrieval import SearchResult


@dataclass(frozen=True)
class GeneratedAnswer:
    text: str
    prompt_tokens: int
    completion_tokens: int


class ModelAdapter:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    async def generate(self, question: str, results: list[SearchResult], max_tokens: int, temperature: float) -> GeneratedAnswer:
        if self.settings.model_base_url:
            return await self._generate_remote(question, results, max_tokens, temperature)
        return self._generate_fallback(question, results)

    async def _generate_remote(self, question: str, results: list[SearchResult], max_tokens: int, temperature: float) -> GeneratedAnswer:
        context = "\n\n".join(f"[{item.chunk.chunk_id}] {item.chunk.text}" for item in results)
        messages = [
            {"role": "system", "content": "Answer only from the supplied context. Say you do not know when the context is insufficient. Cite source IDs like [chunk_id]."},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"},
        ]
        headers = {"Authorization": f"Bearer {self.settings.model_api_key}"} if self.settings.model_api_key else {}
        async with httpx.AsyncClient(timeout=60) as client:
            response = await client.post(
                f"{self.settings.model_base_url.rstrip('/')}/v1/chat/completions",
                headers=headers,
                json={"model": self.settings.model_name, "messages": messages, "max_tokens": max_tokens, "temperature": temperature},
            )
            response.raise_for_status()
            payload = response.json()
        choice = payload["choices"][0]
        usage = payload.get("usage", {})
        return GeneratedAnswer(
            text=choice["message"]["content"],
            prompt_tokens=int(usage.get("prompt_tokens", _count_tokens(question))),
            completion_tokens=int(usage.get("completion_tokens", _count_tokens(choice["message"]["content"]))),
        )

    def _generate_fallback(self, question: str, results: list[SearchResult]) -> GeneratedAnswer:
        if not results:
            text = "I do not have enough grounded information to answer that question."
        else:
            excerpts = []
            for result in results[:3]:
                sentence = re.split(r"(?<=[.!?])\s+", result.chunk.text.strip())[0]
                excerpts.append(f"{sentence} [{result.chunk.chunk_id}]")
            text = "Based on the available public sources: " + " ".join(excerpts)
        return GeneratedAnswer(text=text, prompt_tokens=_count_tokens(question), completion_tokens=_count_tokens(text))


def _count_tokens(text: str) -> int:
    return len(text.split())
