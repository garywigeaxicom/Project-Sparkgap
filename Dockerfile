FROM python:3.12-slim

WORKDIR /app
COPY pyproject.toml README.md ./
COPY src ./src
COPY examples ./examples

RUN pip install --no-cache-dir .

ENV SPARKGAP_CORPUS_DIR=/app/examples/corpus
ENV SPARKGAP_INDEX_PATH=/tmp/sparkgap/index.json

RUN sparkgap-ingest ingest

EXPOSE 8000
CMD ["uvicorn", "sparkgap.app:app", "--host", "0.0.0.0", "--port", "8000"]