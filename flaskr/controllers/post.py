from flask_smorest import abort
from flaskr.extensions import db
from sqlalchemy.exc import SQLAlchemyError

from flaskr.models import PostModel


class PostController:
    def get_posts(self):
        return db.session.execute(db.select(PostModel)).scalars().all()

    def get_post(self, post_id):
        post = db.get_or_404(PostModel, post_id)
        return post

    def create_post(self, post_data):
        post = PostModel(**post_data)

        try:
            db.session.add(post)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=str(e))

        return post

    def update_post(self, post_data, post_id):
        post = db.get_or_404(PostModel, post_id)

        if post:
            post.title = post_data["title"]
            post.content = post_data["content"]

        try:
            db.session.add(post)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=str(e))

        return post

    def delete_post(self, post_id):
        post = db.get_or_404(PostModel, post_id)

        db.session.delete(post)
        db.session.commit()

        return {"message": "Post deleted."}
