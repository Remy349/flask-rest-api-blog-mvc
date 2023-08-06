from flask_smorest import abort
from sqlalchemy.exc import SQLAlchemyError
from flaskr.extensions import db

from flaskr.models import CommentModel, PostModel


class CommentController:
    def get_comments_in_post(self, post_id):
        post = db.get_or_404(PostModel, post_id)
        return post.comments.all()

    def create_comment_in_post(self, comment_data, post_id):
        post = db.get_or_404(PostModel, post_id)

        comment = CommentModel(**comment_data)

        try:
            post.comments.append(comment)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=str(e))

        return comment
