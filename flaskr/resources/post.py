from flask_smorest import Blueprint
from flask.views import MethodView
from flaskr.schemas import PostSchema, PostUpdateSchema
from flaskr.controllers.post import PostController

bp = Blueprint(
    "posts",
    __name__,
    url_prefix="/api",
    description="Operations on posts",
)

controller = PostController()


@bp.route("/post/<int:post_id>")
class Post(MethodView):
    @bp.response(200, PostSchema)
    def get(self, post_id):
        """ Get a single post """
        return controller.get_post(post_id)

    @bp.arguments(PostUpdateSchema)
    @bp.response(200, PostSchema)
    def put(self, post_data, post_id):
        """ Update a post """
        return controller.update_post(post_data, post_id)

    @bp.response(204)
    def delete(self, post_id):
        """ Delete a post """
        return controller.delete_post(post_id)


@bp.route("/post")
class PostList(MethodView):
    @bp.response(200, PostSchema(many=True))
    def get(self):
        """ Get a list of all posts """
        return controller.get_posts()

    @bp.arguments(PostSchema)
    @bp.response(201, PostSchema)
    def post(self, post_data):
        """ Create a new post """
        return controller.create_post(post_data)
