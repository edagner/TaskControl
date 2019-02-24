from functools import wraps
from app.task_orm import User
from flask import request


def require_login(func):
    @wraps(func)
    def check_creds(*args, **kwargs):
        auth = request.authorization
        if auth:
            user = User.query.filter_by(username=auth.username).first()
            pwd_check = user.verify_password(auth.password)
            if not pwd_check:
                return "Unauthorized User, Move Along"
        else:
            return "No Authorized Information received."
        return func(*args, **kwargs)
    return check_creds
