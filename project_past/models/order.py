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
    buy = Column(Boolean(create_constraint=True, name='order_buy_boolean'), nullable=False)
    qty = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    hash = Column(String(32))

    @staticmethod
    def insert_order_hook(items):
        for item in items:
            item['hash'] = uuid4().hex


class OrderHistory(CommonColumns):
    __tablename__ = 'order_history'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, uselist=False)
    order_type = Column(String(80), nullable=False)
    currency = Column(String(80), nullable=False)
    exchange = Column(String(80), nullable=False)
    buy = Column(Boolean(create_constraint=True, name='order_history_buy_boolean'), nullable=False)
    qty = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    status = Column(String(250), nullable=False)

    @staticmethod
    def create_order_history_item(order, status):
        return OrderHistory(
            user_id = order.user_id,
            order_type = order.order_type.name,
            currency = order.currency.name,
            exchange = order.exchange.name,
            buy = order.buy,
            qty = order.qty,
            price = order.price,
            status = status
        )
