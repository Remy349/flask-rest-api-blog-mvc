from flaskr.controllers.post import PostController
from werkzeug.exceptions import NotFound


def test_get_posts_empty(app):
    controller = PostController()
    posts = controller.get_posts()

    assert len(posts) == 0


def test_get_posts(app):
    controller = PostController()

    for index in range(2):
        controller.create_post(
            {
                "title": f"Post {index + 1}",
                "content": f"This is the content of the post {index + 1}",
            }
        )

    posts = controller.get_posts()

    assert len(posts) == 2


def test_get_post_not_found(app):
    controller = PostController()

    try:
        controller.get_post(1)
    except NotFound as e:
        assert e.code == 404
        assert e.name == "Not Found"


def test_get_post(app):
    controller = PostController()

    controller.create_post(
        {
            "title": "Post 1",
            "content": "This is the content of the post 1",
        }
    )

    post = controller.get_post(1)

    assert post.id == 1
    assert post.title == "Post 1"


def test_create_post(app):
    controller = PostController()

    post = controller.create_post(
        {
            "title": "Post 1",
            "content": "This is the content of the post 1",
        }
    )

    assert post is not None


def test_update_post(app):
    controller = PostController()

    post = controller.create_post(
        {
            "title": "Post 1",
            "content": "This is the content of the post 1",
        }
    )

    assert post.title == "Post 1"

    post_update = controller.update_post(
        post_data={
            "title": "Now i change the post title",
            "content": "This is the content of the post 1",
        },
        post_id=1,
    )

    assert post_update.title == "Now i change the post title"


def test_delete_post(app):
    controller = PostController()

    for index in range(2):
        controller.create_post(
            {
                "title": f"Post {index + 1}",
                "content": f"This is the content of the post {index + 1}",
            }
        )

    post = controller.delete_post(1)
    posts = controller.get_posts()

    assert post.get("message") == "Post deleted."
    assert len(posts) == 1
