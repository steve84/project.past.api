from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class CommonColumns(Base):
    __abstract__ = True
    _created = Column(DateTime, default=func.now())
    _updated = Column(DateTime, default=func.now(), onupdate=func.now())
    _etag = Column(String(40))


class Exchange(CommonColumns):
    __tablename__ = 'exchange'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80))
    

class Order(CommonColumns):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True, autoincrement=True)
    exchange_id = Column(Integer, ForeignKey('exchange.id'))
    exchange = relationship(Exchange, uselist=False)