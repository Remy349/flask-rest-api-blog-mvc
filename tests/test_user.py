from flaskr.controllers.user import UserController
from werkzeug.exceptions import Conflict, NotFound


def test_do_not_create_user_twice(app):
    controller = UserController()

    try:
        for _ in range(2):
            controller.create_user(
                {
                    "username": "user1",
                    "password": "user1234",
                }
            )
    except Conflict as e:
        assert e.name == "Conflict"
        assert e.code == 409


def test_create_user(app):
    controller = UserController()

    user = controller.create_user(
        {
            "username": "user1",
            "password": "user1234",
        }
    )

    assert user.get("message") == "User created successfully."


def test_get_user_not_found(app):
    controller = UserController()

    try:
        controller.get_user(1)
    except NotFound as e:
        assert e.code == 404
        assert e.name == "Not Found"


def test_get_user(app):
    controller = UserController()

    controller.create_user({"username": "user1", "password": "user1234"})

    user = controller.get_user(1)

    assert user is not None
    assert user.username == "user1"


def test_delete_user(app):
    controller = UserController()

    controller.create_user({"username": "user1", "password": "user1234"})

    user = controller.delete_user(1)

    assert user.get("message") == "User deleted."
