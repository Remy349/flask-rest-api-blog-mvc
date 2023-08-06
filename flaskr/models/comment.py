import sqlalchemy as sa
from datetime import datetime
from flaskr.extensions import db


class CommentModel(db.Model):
    __tablename__ = "comments"

    id = sa.Column(sa.Integer, primary_key=True)
    content = sa.Column(sa.String(300), nullable=False, unique=False)
    create_at = sa.Column(sa.DateTime, default=datetime.utcnow)

    post_id = sa.Column(
        sa.Integer,
        sa.ForeignKey("posts.id"),
        nullable=False,
        unique=False,
    )

    post = db.relationship("PostModel", back_populates="comments")
