import requests
from werkzeug.exceptions import BadRequest

from .encryption import get_signature


bybit_public_api_url = 'https://api-testnet.bybit.com/v2/public'

def get_bybit_timestamp():
    req_timestamp = requests.get(bybit_public_api_url + '/time')
    json_response = req_timestamp.json()
    status_code = req_timestamp.status_code
    return_code = json_response['ret_code']
    if status_code == requests.codes.ok and return_code == 0 and 'time_now' in json_response:
        bybit_time = json_response['time_now']
        if bybit_time is not None and len(bybit_time.split('.')) == 2:
            return int(bybit_time.split('.')[0])
        else:
            raise BadRequest('Unexpected ByBit server time request body.')

    raise BadRequest('Requesting ByBit server time failed.')


def setup_bybit_params(order):
        params = dict()
        params['timestamp'] = get_bybit_timestamp()
        params['side'] = 'Buy' if order.buy else 'Sell'
        params['symbol'] = order.currency.crypto_currency + order.currency.forex_currency
        params['order_type'] = order.order_type.name
        params['qty'] = order.qty
        params['price'] = order.price
        params['time_in_force'] = 'GoodTillCancel'
        params['api_key'] = 'key'
        params = dict(sorted(params.items()))
        params['sign'] = get_signature('123', params)
