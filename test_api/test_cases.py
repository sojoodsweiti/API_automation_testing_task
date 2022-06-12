import requests
import pytest

# API url
base_url = "https://jsonplaceholder.typicode.com"


# Submit a GET request to https://jsonplaceholder.typicode.com/posts
# Check that the response status code is equal to 200
# Check that the response body is a list (an array) containing 100 elements
# Positive case of get the posts
def test_get_posts_positive():
    response = requests.get(base_url + "/posts")
    response_body = response.json()
    assert len(response_body) == 100
    print(response.status_code)
    # validation of response code
    assert response.status_code == 200


# Submit a GET request to https://jsonplaceholder.typicode.com/posts
# Check that the response status code is equal to 401
# Negative case of get the posts]
def test_get_posts_negative():
    response = requests.get(base_url + "/posts")
    response_body = response.json()
    assert len(response_body) == 9
    # validation of response code
    assert response.status_code == 401


# Submit a GET request to https://jsonplaceholder.typicode.com/posts/1
# Check that the response status code is equal to 200
# Check that the response body field 'id' exists
# Positive case of get the posts_1
def test_get_posts1_positive():
    response = requests.get(base_url + "/posts/1")
    response_body = response.json()
    assert 'id' in response_body
    # validation of response code
    assert response.status_code == 200


# Submit a GET request to https://jsonplaceholder.typicode.com/posts/1
# Check that the response status code is equal to 401
# Check that the response body field 'name' doesn't exist
# negative case of get the posts_1
def test_get_posts1_negative():
    response = requests.get(base_url + "/posts/1")
    response_body = response.json()
    assert 'name' in response_body
    # validation of response code
    assert response.status_code == 401


# Submit a GET request to https://jsonplaceholder.typicode.com/comments?postId=1
# Check that the response body field 'email' has a value equal to 'Eliseo@gardner.biz'
# Positive case of get comments postid = 1

test_data_users = [(1, "Eliseo@gardner.biz")]

@pytest.mark.parametrize("postId, expected_email", test_data_users)
def test_get_comment_positive(postId, expected_email):
    response = requests.get(base_url + f"/comments?postId=1/{postId}")
    response_body = response.json()
    print(response.status_code)
    assert response.status_code == 200


# Submit a GET request to https://jsonplaceholder.typicode.com/comments?postId=1
# Check that the response body field 'email' has a value equal to 'abc@gmail.com'
# Negative case of get comments postid = 1
def test_get_comment_negative():
    response = requests.get(base_url + "/comments?postId=1/")
    response_body = response.json()
    assert 'email' in response_body == "abc@gmail.com"
    assert response.status_code == 401


# Submit a POST request to https://jsonplaceholder.typicode.com/posts
# to create a new post with a title, body and associated user ID (1-10)
# Check that the response status code equals HTTP 201 (Created)
def test_post_new_post():
    new_post = {
        "title": "My new post title",
        "body": "My new post body",
        "userId": 1
    }
    response = requests.post(base_url + "/posts", json=new_post)
    response_body = response.json()
    print(response.status_code)
    # validation of response code
    assert response.status_code == 201


# Negative case of create a new post in posts
def test_post_new_post_negative():
    new_post = {
        "title": "new post title",
        "body": " new post body",
        "userId": 2
    }
    response = requests.post(base_url + "/posts")
    response_body = response.json()
    print(response.status_code)
    assert "name" in response_body == "Eliseo"


# Positive case of delete the posts/1
def test_delete_posts_1_positive():
    response = requests.delete(base_url + "/posts/1")
    print(response.status_code)
    # validation of response code of delete is 200 or 204
    assert response.status_code == 200


# Negative case of delete the posts/1
def test_delete_posts_1_negative():
    response = requests.delete(base_url + "//posts/1")
    response_body = response.json()
    assert "email" in response_body

