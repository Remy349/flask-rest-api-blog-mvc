from flask_smorest import Blueprint
from flask.views import MethodView
from flaskr.controllers.comment import CommentController
from flaskr.schemas import CommentSchema

bp = Blueprint(
    "comments",
    __name__,
    url_prefix="/api",
    description="Operations on comments",
)

controller = CommentController()


@bp.route("/post/<int:post_id>/comment")
class CommentInPostList(MethodView):
    @bp.response(200, CommentSchema(many=True))
    def get(self, post_id):
        """ Get a list of all comments in a post """
        return controller.get_comments_in_post(post_id)

    @bp.arguments(CommentSchema)
    @bp.response(201, CommentSchema)
    def post(self, comment_data, post_id):
        """ Create a new comment in a post """
        return controller.create_comment_in_post(comment_data, post_id)
