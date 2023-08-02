from datetime import datetime
import sqlalchemy as sa
from flaskr.extensions import db


class PostModel(db.Model):
    __tablename__ = "posts"

    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String(200), nullable=False, unique=False)
    content = sa.Column(sa.Text, nullable=False, unique=False)
    create_at = sa.Column(sa.DateTime, default=datetime.utcnow)
