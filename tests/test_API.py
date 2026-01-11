import requests
import pytest
import conftest
from clients.get_client import GetClient
from tests.conftest import get_client


def test_GET(get_client):
    response = get_client.get_data()
    assert response.status_code == 200




def test_POST(base_url,session):
    data = {
        "user_id": 1682,
        "title": "priveeeet"
    }
    res_post = session.post(f"{base_url}/posts", json=data)
    assert res_post.json()["user_id"] == data["user_id"]
    assert res_post.json()["title"] == data["title"]

def test_PUT(base_url,session):
    data_put ={
        "user_id": 1683,
        "title": "ne priveeeet"
    }
    res_put = session.put(f"{base_url}/posts/1", json=data_put)
    assert res_put.json()["user_id"] == data_put["user_id"]


def test_PATCH(base_url,session):
    data_patch = {
        "title":"hello world!"
    }
    res_patch = session.patch(f"{base_url}posts/1", json=data_patch)
    assert res_patch.json()["title"] == data_patch["title"]

def test_DELETE(base_url,session):
    res_delete = session.delete(f"{base_url}/posts/1")
    assert res_delete.json() == {}
