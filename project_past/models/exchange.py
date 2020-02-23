from sqlalchemy import Column, Integer, String

from .base import CommonColumns


class Exchange(CommonColumns):
    __tablename__ = 'exchange'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80))
