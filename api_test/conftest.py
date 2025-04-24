import pytest
from config.env_config import ENVIRONMENTS
from utils.api_client import APIClient

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="qa")

@pytest.fixture(scope="session")
def base_url(pytestconfig):
    env = pytestconfig.getoption("env")
    return ENVIRONMENTS[env]

@pytest.fixture(scope="session")
def client(base_url):
    return APIClient(base_url)

