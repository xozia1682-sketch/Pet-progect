import requests


def test_neg_GET():
    res_get = requests.get("https://jsonplaceholder.typicode.com/999")
    assert res_get.status_code == 404
def test_neg_POST():
    data_post = {
        "title":"",
        "content":""
    }
    res_post = requests.post("https://jsonplaceholder.typicode.com/posts",json=data_post)
    assert res_post.json()["title"] == data_post["title"]
def test_neg_PUT():
    data_put = {
        "jumaisa":123445
    }
    res_put = requests.put("https://jsonplaceholder.typicode.com/posts",json=data_put)
    assert res_put.json() == {}


