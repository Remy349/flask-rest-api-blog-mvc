from flask.views import MethodView
from flask_smorest import Blueprint
from flaskr.schemas import UserSchema
from flaskr.controllers.user import UserController

bp = Blueprint(
    "users",
    __name__,
    url_prefix="/api",
    description="Operations on users",
)

controller = UserController()


@bp.route("/register")
class UserRegister(MethodView):
    @bp.arguments(UserSchema)
    @bp.response(201)
    def post(self, user_data):
        return controller.create_user(user_data)


@bp.route("/user/<int:user_id>")
class User(MethodView):
    @bp.response(200, UserSchema)
    def get(self, user_id):
        return controller.get_user(user_id)

    @bp.response(204)
    def delete(self, user_id):
        return controller.delete_user(user_id)
