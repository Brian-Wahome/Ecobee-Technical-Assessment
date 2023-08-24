import requests
import random

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


def main():
    print("Welcome to the Ecobee blog!")
    print("Choose an option from the list below: ")
    print("1. View posts")
    print("2. Search for post")
    print("3. Exit application")
    option = int(input("Select option number: "))

    if option == 1:
        # get 10 random posts
        posts = random.sample(get_posts(), 10)
        # display posts
        for post in posts:
            print(f"PostId: {post['id']}, Title: {post['title']}")
            continue
        # select post to view
        post_id = int(input("Select ID of post you wish to view: "))
        post = select_post(post_id)

        if post:
            print(
                f"\nAuthorID ID: {post['userId']}\nPost ID: {post['id']}\nTitle: {post['title']}\nBody: {post['body']}\n")
            # view comments
            option_to_view_comment = int(input("Key in 1 if you wish to view the comments on this post: "))
            if option_to_view_comment == 1:
                comments = view_post_comments(post_id)
                print("\nComments:")
                for comment in comments:
                    print(f"Name: {comment['name']}\nEmail: {comment['email']}\nBody: {comment['body']}\n")
            # option to create comment
            option_to_comment = int(input("Key in 1 if you wish to comment: "))
            if option_to_comment == 1:
                name = input("Enter your name: ")
                email = input("Enter your email: ")
                body = input("Enter your comment: ")
                if post_comment(post_id, name, email, body):
                    print("Comment posted successfully!")
                else:
                    print("Failed to post comment.")
        else:
            print(f"Post with ID {post_id} not found.")

    elif option == 2:
        # Search for posts by title
        title = input("Enter a title or part of title to search for: ")
        matching_posts = search_posts_by_title(title)
        if matching_posts:
            print("Matching Posts:")
            for post in matching_posts:
                print(f"Post ID: {post['id']}, Title: {post['title']}")
                continue

            # select post to view
            post_id = int(input("Select ID of post you wish to view: "))
            post = select_post(post_id)

            if post:
                print(
                    f"\nAuthorID ID: {post['userId']}\nPost ID: {post['id']}\nTitle: {post['title']}\nBody: {post['body']}\n")
                # view comments
                option_to_view_comment = int(input("Key in 1 if you wish to view the comments on this post: "))
                if option_to_view_comment == 1:
                    comments = view_post_comments(post_id)
                    print("\nComments:")
                    for comment in comments:
                        print(f"Name: {comment['name']}\nEmail: {comment['email']}\nBody: {comment['body']}\n")
                # option to create comment
                option_to_comment = int(input("Key in 1 if you wish to comment: "))
                if option_to_comment == 1:
                    name = input("Enter your name: ")
                    email = input("Enter your email: ")
                    body = input("Enter your comment: ")
                    if post_comment(post_id, name, email, body):
                        print("Comment posted successfully!")
                    else:
                        print("Failed to post comment.")
            else:
                print(f"Post with ID {post_id} not found.")
        else:
            print("No matching posts found.")

    elif option == 3:
        print("Exited app successfully")
        global running
        running = False


if __name__ == "__main__":
    running = True
    while running:
        main()
