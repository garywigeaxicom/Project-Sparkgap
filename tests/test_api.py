from fastapi.testclient import TestClient

from sparkgap.app import app


client = TestClient(app)


def test_health() -> None:
    response = client.get("/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_missing_tenant_is_rejected() -> None:
    response = client.post(
        "/v1/chat/completions",
        json={"model": "reference-fallback", "messages": [{"role": "user", "content": "What is this project?"}]},
    )
    assert response.status_code == 400
    assert response.json()["error"]["code"] == "missing_tenant"


def test_high_impact_request_is_refused() -> None:
    response = client.post(
        "/v1/chat/completions",
        headers={"X-Tenant-ID": "public-demo", "X-Request-ID": "test-request"},
        json={"model": "reference-fallback", "messages": [{"role": "user", "content": "Decide whether a person should receive essential services."}]},
    )
    assert response.status_code == 200
    assert response.json()["choices"][0]["finish_reason"] == "safety"
