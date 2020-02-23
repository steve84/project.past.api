from sqlalchemy import Column, Integer, String

from .base import CommonColumns


class User(CommonColumns):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80))
    username = Column(String(80))
    password = Column(String(80))


class UserExchangeSetting(CommonColumns):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80))
