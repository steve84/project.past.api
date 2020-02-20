from flask import Blueprint, request

order_routes = Blueprint('order_api', __name__)

@order_routes.route('/add/<exchange_id>', methods=['POST'])
def addOrder(exchange_id):
    if 'name' in request.json:
        return "add order %s" % request.json['name']
    else:
        return "not found"