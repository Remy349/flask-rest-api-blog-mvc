from flask_jwt_extended import create_access_token
from flaskr.extensions import db
from flask_smorest import abort

from flaskr.models import UserModel


class UserController:
    def login_user(self, user_data):
        user = db.session.execute(
            db.select(UserModel).filter_by(username=user_data["username"])
        ).scalar_one_or_none()

        if user and user.check_password(user_data["password"]):
            access_token = create_access_token(identity=user.id)
            return {"access_token": access_token}

        abort(401, message="Invalid credentials.")

    def get_user(self, user_id):
        return db.get_or_404(UserModel, user_id)

    def create_user(self, user_data):
        if db.session.execute(
            db.select(UserModel).filter_by(username=user_data["username"])
        ).first():
            abort(409, message="A user with that username already exists.")

        user = UserModel(username=user_data["username"])
        user.set_password(password=user_data["password"])

        db.session.add(user)
        db.session.commit()

        return {"message": "User created successfully."}

    def delete_user(self, user_id):
        user = db.get_or_404(UserModel, user_id)

        db.session.delete(user)
        db.session.commit()

        return {"message": "User deleted."}
