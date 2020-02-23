from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import CommonColumns


class Currency(CommonColumns):
    __tablename__ = 'currency'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80))
    forex_currency = Column(String(3))
    crypto_currency = Column(String(3))
