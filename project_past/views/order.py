from flask import Blueprint, request
from flask_sqlalchemy import SQLAlchemy
import requests

from project_past.models import Order, OrderHistory
from project_past.utils import get_signature


order_bp = Blueprint('order_api', __name__)

db = SQLAlchemy()


@order_bp.route('/add', methods=['POST'])
def addOrder():
    if 'order_id' in request.json and 'hash' in request.json:
        order = db.session.query(Order).filter(Order.id == int(request.json['order_id'])).first()
        if order.hash != request.json['hash']:
            return 'wrong hash'
        else:
            params = dict()
            req_timestamp = requests.get('https://api-testnet.bybit.com/v2/public/time')
            if req_timestamp.status_code == requests.codes.ok and req_timestamp.json()['ret_code'] == 0:
                params['timestamp'] = int(req_timestamp.json()['time_now'].split('.')[0])
            params['side'] = 'Buy' if order.buy else 'Sell'
            params['symbol'] = order.currency.crypto_currency + order.currency.forex_currency
            params['order_type'] = order.order_type.name
            params['qty'] = order.qty
            params['price'] = order.price
            params['time_in_force'] = 'GoodTillCancel'
            params['api_key'] = 'key'
            params = dict(sorted(params.items()))
            params['sign'] = get_signature('123', params)
            print('&'.join([str(k)+"="+str(v) for k, v in params.items()]))
            #req_to_exchange = requests.post('https://httpbin.org/get', params=params)
            #if req_to_exchange.status_code == requests.codes.ok and req_to_exchange.json()['ret_code'] == 0:
            #    OrderHistory(order_id=order.id, status='OK')
            order_history = OrderHistory(order_id=order.id, status='OK')
            db.session.add(order_history)
            db.session.commit()
            return 'add order %s' % request.json['order_id']
    else:
        return 'not found'