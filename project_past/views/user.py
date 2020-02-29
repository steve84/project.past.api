import json
from base64 import b64encode

from flask import Blueprint, request, jsonify, current_app as app
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import Unauthorized

from project_past.models import User
from project_past.utils import get_signature


user_bp = Blueprint('user_api', __name__)


@user_bp.route('/login', methods=['POST'])
def login():
    """Simple login view that expect to have username
    and password in the request POST. If the username and
    password matches - token is being generated and return.
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        raise Unauthorized('Wrong username and/or password.')
    else:
        user = app.data.driver.session.query(User).filter(User.username == username).first()
        if user and user.check_password(password):
            token = user.generate_auth_token()
            return jsonify({'token': b64encode(token)})
    raise Unauthorized('Wrong username and/or password.')