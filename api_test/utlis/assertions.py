def assert_status_code(response, expected):
    assert response.status_code == expected, f"Expected {expected}, got {response.status_code}"

def assert_json_keys(json_data, keys):
    for key in keys:
        assert key in json_data, f"Missing key: {key}"

