import requests

API_URL = "https://jsonplaceholder.typicode.com"


def get_posts():
    response = requests.get(f"{API_URL}/posts")
    if response.status_code == 200:
        return response.json()
    return []


def select_post(post_id):
    response = requests.get(f"{API_URL}/posts/{post_id}")
    if response.status_code == 200:
        return response.json()
    return "Post Id does not exist"
