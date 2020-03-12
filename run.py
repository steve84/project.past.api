from project_past import create_app
from project_past.models import Currency, Exchange, Order, OrderType, User


app = create_app()
db = app.data.driver

if not db.session.query(Order).count():
    user = User(name='Bob', username='bob', password='1234', role='admin')
    currency = Currency(name='BTCUSD', crypto_currency='BTC', forex_currency='USD')
    exchange = Exchange(name='ByBit')
    order_type1 = OrderType(name='Limit')
    order_type2 = OrderType(name='Market')
    db.session.add_all([
            user,
            currency,
            exchange,
            order_type1,
            order_type2])
    db.session.commit()
    for i in range(0,100):
        db.session.add(Order(
                user_id=user.id, currency_id=currency.id,
                order_type_id=order_type1.id, exchange_id=exchange.id,
                buy=True, price=i+0.23, qty=i, hash='1234'))
    db.session.commit()


if __name__ == '__main__':
    app.run(debug=True, port=5000)
