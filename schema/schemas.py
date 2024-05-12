def individual_serial(post) -> dict:
    return {
        "id": str(post["_id"]),
        "title": post["title"],
        "content": post["content"],
        "comments":post["comments"],
        "likes":post["likes"],
        "dislikes": post["dislikes"]
    }

def list_serial(posts):
    return[individual_serial(post) for post in posts ]
