import requests

API_URL = "https://jsonplaceholder.typicode.com"


def get_posts():
    response = requests.get(f"{API_URL}/posts")
    if response.status_code == 200:
        return response.json()
    return []