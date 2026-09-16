from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Settings:
    model_base_url: str | None
    model_api_key: str | None
    model_name: str
    corpus_dir: Path
    index_path: Path

    @classmethod
    def from_env(cls) -> Settings:
        return cls(
            model_base_url=os.getenv("SPARKGAP_MODEL_BASE_URL") or None,
            model_api_key=os.getenv("SPARKGAP_MODEL_API_KEY") or None,
            model_name=os.getenv("SPARKGAP_MODEL_NAME", "reference-fallback"),
            corpus_dir=Path(os.getenv("SPARKGAP_CORPUS_DIR", "examples/corpus")),
            index_path=Path(os.getenv("SPARKGAP_INDEX_PATH", ".sparkgap/index.json")),
        )
