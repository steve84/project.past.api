from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import CommonColumns
from .exchange import Exchange


class User(CommonColumns):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80))
    username = Column(String(80))
    password = Column(String(80))


class UserExchangeSetting(CommonColumns):
    __tablename__ = 'user_exchange_setting'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, uselist=False)
    exchange_id = Column(Integer, ForeignKey('exchange.id'))
    exchange = relationship(Exchange, uselist=False)