from base64 import b64decode

from eve import Eve
from eve.auth import TokenAuth
from flask import current_app as app

from project_past.models import Base, User

class RolesAuth(TokenAuth):
    def check_auth(self, token, allowed_roles, resource, method):
        """First we are verifying if the token is valid. Next
        we are checking if user is authorized for given roles.
        """
        token = b64decode(token.split('Basic')[1])
        id = User.verify_auth_token(token)
        if id and allowed_roles:
            user = app.data.driver.session.query(User).get(id)
            return user.isAuthorized(allowed_roles)
        else:
            return False
