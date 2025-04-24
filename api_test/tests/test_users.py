import pytest
from utils.assertions import assert_status_code, assert_json_keys

@pytest.mark.flaky(reruns=2)
def test_get_users(client):
    res = client.get("/users")
    assert_status_code(res, 200)
    assert isinstance(res.json(), list)

@pytest.mark.parametrize("user", [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"}
])
def test_create_user(client, user):
    res = client.post("/users", json=user)
    assert_status_code(res, 201)
    assert_json_keys(res.json(), ["id", "name", "email"])

