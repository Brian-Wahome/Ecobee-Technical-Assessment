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


def view_post_comments(post_id):
    response = requests.get(f"{API_URL}/posts/{post_id}/comments")
    if response.status_code == 200:
        return response.json()
    return "No comments"


def post_comment(post_id, name, email, body):
    comment_id = 500
    comment = {
        "id": comment_id + 1,
        "name": name,
        "email": email,
        "body": body
    }
    response = requests.post(f"{API_URL}/posts/{post_id}/comments", json=comment)

    return response.status_code == 201


def search_posts_by_title(title):
    posts = get_posts()
    matching_posts = []
    for post in posts:
        if title.lower() in post['title'].lower():
            matching_posts.append(post)
    return matching_posts


