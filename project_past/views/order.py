from flask import Blueprint, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import BadRequest
import requests

from project_past.models import Order, OrderHistory


order_bp = Blueprint('order_api', __name__)

db = SQLAlchemy()


@order_bp.route('/add', methods=['POST'])
def addOrder():
    data = request.get_json()
    order_id = data.get('order_id')
    order_hash = data.get('hash')

    if not order_id or not order_hash:
        raise BadRequest('Order id and hash not found.')

    order = db.session.query(Order).filter(Order.id == int(order_id)).first()
    if order.hash != order_hash:
        raise BadRequest('Wrong order hash provided.')
    else:
        params = setup_bybit_params(order)
        #req_to_exchange = requests.post('https://httpbin.org/get', params=params)
        #if req_to_exchange.status_code == requests.codes.ok and req_to_exchange.json()['ret_code'] == 0:
        #    OrderHistory(order_id=order.id, status='OK')
        order_history = OrderHistory(order_id=order.id, status='OK')
        db.session.add(order_history)
        db.session.commit()
        return 'add order %s' % request.json['order_id']