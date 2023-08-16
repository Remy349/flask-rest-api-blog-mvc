from flaskr.controllers.post import PostController


def test_get_posts_empty(app):
    controller = PostController()
    posts = controller.get_posts()

    assert len(posts) == 0
