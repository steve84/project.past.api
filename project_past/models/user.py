from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, validates
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired, BadSignature

from .base import CommonColumns
from .exchange import Exchange

SECRET_KEY = 'this-is-my-super-secret-key'


class User(CommonColumns):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80))
    username = Column(String(80), unique=True)
    password = Column(String(80))
    role = Column(String(80))
    
    def generate_auth_token(self, expiration=24*60*60):
        """Generates token for given expiration
        and user login."""
        s = Serializer(SECRET_KEY, expires_in=expiration)
        return s.dumps({'id': self.id })


    @staticmethod
    def verify_auth_token(token):
        """Verifies token and eventually returns
        user login.
        """
        s = Serializer(SECRET_KEY)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None # valid token, but expired
        except BadSignature:
            return None # invalid token
        return data['id']


    def isAuthorized(self, role_names):
        """Checks if user is related to given role_names.
        """
        if role_names is None or len(role_names) == 0:
            return True
        return self.role and self.role in role_names

    def encrypt(self, password):
        """Encrypt password using werkzeug security module.
        """
        return generate_password_hash(password)

        
    @validates('password')
    def _set_password(self, key, value):
        """Using SQLAlchemy validation makes sure each
        time password is changed it will get encrypted
        before flushing to db.
        """
        return self.encrypt(value)


    def check_password(self, password):
        if not self.password:
            return False
        return check_password_hash(self.password, password)


class UserExchangeSetting(CommonColumns):
    __tablename__ = 'user_exchange_setting'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, uselist=False)
    exchange_id = Column(Integer, ForeignKey('exchange.id'))
    exchange = relationship(Exchange, uselist=False)
