from __future__ import annotations

import argparse

from .config import Settings
from .ingestion import ingest_directory


def main() -> None:
    parser = argparse.ArgumentParser(description="Project Sparkgap utilities")
    subparsers = parser.add_subparsers(dest="command", required=True)
    ingest = subparsers.add_parser("ingest", help="Index Markdown and text documents")
    ingest.add_argument("--source", default=None)
    ingest.add_argument("--output", default=None)
    args = parser.parse_args()
    settings = Settings.from_env()
    if args.command == "ingest":
        chunks = ingest_directory(
            settings.corpus_dir if args.source is None else __import__("pathlib").Path(args.source),
            settings.index_path if args.output is None else __import__("pathlib").Path(args.output),
        )
        print(f"Indexed {len(chunks)} chunks.")
