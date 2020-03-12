from eve import Eve
from eve_sqlalchemy import SQL
from eve_sqlalchemy.validation import ValidatorSQL

from project_past.models import Base, Order
from project_past.utils import RolesAuth

def create_app():
    from . import views
    #app = Eve(validator=ValidatorSQL, data=SQL, auth=RolesAuth)
    app = Eve(validator=ValidatorSQL, data=SQL)
    db = app.data.driver
    Base.metadata.bind = db.engine
    db.Model = Base
    db.create_all()
    views.init_app(app)

    app.on_insert_order += Order.insert_order_hook

    return app