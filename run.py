from eve import Eve
from eve_sqlalchemy import SQL
from eve_sqlalchemy.validation import ValidatorSQL
from model import Base, Exchange
from project_past.views import order_routes
from project_past.models import Base, Exchange

app = Eve(validator=ValidatorSQL, data=SQL)

app.register_blueprint(order_routes, url_prefix='/order')

db = app.data.driver
Base.metadata.bind = db.engine
db.Model = Base
db.create_all()




if not db.session.query(Exchange).count():
    db.session.add_all([
        Exchange(name='ByBit'),
        Exchange(name='TestExchange')])
    db.session.commit()


if __name__ == '__main__':
    app.run()
