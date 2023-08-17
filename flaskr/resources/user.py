from flask.views import MethodView
from flask_smorest import Blueprint

bp = Blueprint(
    "users",
    __name__,
    url_prefix="/api",
    description="Operations on users",
)
