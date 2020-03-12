from eve_sqlalchemy.config import DomainConfig, ResourceConfig

from project_past.models import Currency, Exchange, Order, OrderHistory, OrderType, User

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/project_past'
SQLALCHEMY_TRACK_MODIFICATIONS = False
RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET', 'PUT', 'PATCH']

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


DOMAIN['user']['datasource'].update({
    'projection': {'username': 1, 'name': 1}
})

DOMAIN['order']['schema']['user']['data_relation']['embeddable'] = True
DOMAIN['order']['schema']['exchange']['data_relation']['embeddable'] = True
DOMAIN['order']['schema']['currency']['data_relation']['embeddable'] = True
DOMAIN['order']['schema']['order_type']['data_relation']['embeddable'] = True


DOMAIN['order'].update({
    'allowed_roles': ['admin']
})
