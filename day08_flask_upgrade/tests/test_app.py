import pytest

from app import app


@pytest.fixture
def client():
    app.config.update(TESTING=True, SECRET_KEY="day08-test-key")
    with app.test_client() as test_client:
        yield test_client


def login(client):
    return client.post("/login", data={"username": "student", "password": "day07"})


def test_health_returns_json(client):
    response = client.get("/health")
    body = response.get_json()
    assert response.status_code == 200
    assert body == {
        "ok": True,
        "service": "day08-flask-upgrade",
        "student_id": "24012412",
    }


def test_metrics_rejects_unauthenticated_request(client):
    response = client.get("/api/metrics")
    assert response.status_code == 401
    assert response.get_json() == {"ok": False, "error": "请先登录。"}


def test_metrics_comes_from_data_service(client):
    login(client)
    response = client.get("/api/metrics")
    body = response.get_json()
    assert response.status_code == 200
    assert body["ok"] is True
    assert body["metrics"][0] == {"label": "总用户数", "value": "5,630", "note": "人"}
    assert len(body["metrics"]) == 4


def test_category_filter_changes_rows(client):
    login(client)
    all_rows = client.get("/api/categories").get_json()["rows"]
    fashion_response = client.get("/api/categories?category=Fashion")
    fashion_rows = fashion_response.get_json()["rows"]
    assert fashion_response.status_code == 200
    assert len(all_rows) == 5
    assert len(fashion_rows) == 1
    assert fashion_rows[0]["偏好品类"] == "Fashion"
    assert fashion_rows != all_rows


def test_unknown_category_returns_400(client):
    login(client)
    response = client.get("/api/categories?category=Unknown")
    assert response.status_code == 400
    assert response.get_json() == {"ok": False, "error": "不存在的品类。"}


def test_ask_rejects_non_json_body(client):
    login(client)
    response = client.post("/api/ask", data="question=用户数")
    assert response.status_code == 400
    assert response.get_json() == {"ok": False, "error": "请求格式不正确。"}


def test_dashboard_keeps_original_page_available(client):
    login(client)
    response = client.get("/dashboard?category=Fashion")
    content = response.get_data(as_text=True)
    assert response.status_code == 200
    assert "电商用户行为数据看板" in content
    assert "Fashion" in content
