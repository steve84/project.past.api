from eve_sqlalchemy.config import DomainConfig, ResourceConfig

from project_past.models import Currency, Exchange, Order, OrderHistory, OrderType, User

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/project_past'
SQLALCHEMY_TRACK_MODIFICATIONS = False
RESOURCE_METHODS = ['GET', 'POST']

# The following two lines will output the SQL statements executed by
# SQLAlchemy. This is useful while debugging and in development, but is turned
# off by default.
# --------
# SQLALCHEMY_ECHO = True
# SQLALCHEMY_RECORD_QUERIES = True

# The default schema is generated using DomainConfig:
DOMAIN = DomainConfig({
    'currency': ResourceConfig(Currency),
    'exchange': ResourceConfig(Exchange),
    'order': ResourceConfig(Order),
    'order_history': ResourceConfig(OrderHistory),
    'order_type': ResourceConfig(OrderType),
    'user': ResourceConfig(User),
}).render()
