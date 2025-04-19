import os
import json
from datetime import datetime

file_dir = r"E:\Python\test cases\Social JSON\social.json"

def user_exists(name):
    with open(file_dir, "r") as f:
        data = json.load(f)

    for user in data["users"]:
        if user["username"].lower() == name.lower():
            return [True, user]
            break

    return [False, None]


def create_user(name):

    if os.path.exists(file_dir) and os.path.getsize(file_dir) > 0:
        with open(file_dir, "r") as f:
            data = json.load(f)

    else:
        data = {"users": []}

    new_user_data = {
        "username": name,
        "posts": []
    }

    if user_exists(name)[0]:
        print(f"User {name} already exists.")
        return

    data["users"].append(new_user_data)

    with open(file_dir, "w") as f:
        json.dump(data, f, indent=4)

    print(f"User {name} created successfully!")


def add_post(new_post, name):

    with open(file_dir, "r") as f:
        data = json.load(f)

    user_found = False

    if user_exists(name)[0]:
        user = user_exists(name)[1]
        user["posts"].append({
            "content": new_post,
            "timestamp": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            "edited": False
        })

        with open(file_dir, "w") as f:
            json.dump(data, f, indent=4)
        print("Post added !")

    else:
        print(f"User {name} not found :(")


def print_posts(user):
    print(f'User: {user["username"]}')
    for post in user["posts"]:
        if isinstance(post, dict):
            print(f'    [{post["timestamp"]}] {post["content"]}')
        else:
            print(f"    {post}")


def view_post(name="all"):

    with open(file_dir, "r") as f:
        data = json.load(f)

    if name == "all":
        for user in data["users"]:
            print_posts(user)

    else:

        if user_exists(name)[0]:
            user = user_exists(name)[1]
            print_posts(user)

        else:
            print(f"User {name} not found :(")


def delete_user(name):
    user_found = False


