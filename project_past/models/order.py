from uuid import uuid4
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship

from .base import CommonColumns
from .currency import Currency
from .exchange import Exchange
from .user import User

class OrderType(CommonColumns):
    __tablename__ = 'order_type'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80))


class Order(CommonColumns):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_type_id = Column(Integer, ForeignKey('order_type.id'))
    order_type = relationship(OrderType, uselist=False)
    currency_id = Column(Integer, ForeignKey('currency.id'))
    currency = relationship(Currency, uselist=False)
    exchange_id = Column(Integer, ForeignKey('exchange.id'))
    exchange = relationship(Exchange, uselist=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, uselist=False)
    buy = Column(Boolean(create_constraint=True, name='order_buy_boolean'))
    qty = Column(Integer)
    price = Column(Float)
    hash = Column(String(32))

    @staticmethod
    def insert_order_hook(items):
        import pdb;pdb.set_trace()
        for item in items:
            item.hash = uuid4().hex


class OrderHistory(CommonColumns):
    __tablename__ = 'order_history'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('order.id'))
    order = relationship(Order, uselist=False)
    status = Column(String(80))
