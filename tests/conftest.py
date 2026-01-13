import pytest
import requests
from clients.get_client import GetClient


@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com/"

@pytest.fixture
def session():
    return requests.Session()

@pytest.fixture
def get_client(session,base_url):
    return GetClient(session,base_url)
