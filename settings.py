from eve_sqlalchemy.config import DomainConfig, ResourceConfig
from model import Exchange, Order

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
    'exchange': ResourceConfig(Exchange),
    'order': ResourceConfig(Order)
}).render()

RENDERERS = [
    'eve.render.JSONRenderer',
    #'eve.render.XMLRenderer'
]