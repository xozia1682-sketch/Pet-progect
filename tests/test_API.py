import requests

def test_GET():
    response = requests.get("https://jsonplaceholder.typicode.com/")
    assert response.status_code == 200


def test_POST():
    data = {
        "user_id": 1682,
        "title": "priveeeet"
    }
    res_post = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)
    assert res_post.json()["user_id"] == data["user_id"]
    assert res_post.json()["title"] == data["title"]

def test_PUT():
    data_put ={
        "user_id": 1683,
        "title": "ne priveeeet"
    }
    res_put = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=data_put)
    assert res_put.json()["user_id"] == data_put["user_id"]


def test_PATCH():
    data_patch = {
        "title":"hello world!"
    }
    res_patch = requests.patch("https://jsonplaceholder.typicode.com/posts/1", json=data_patch)
    assert res_patch.json()["title"] == data_patch["title"]

def test_DELETE():
    res_delete = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
    assert res_delete.json() == {}
