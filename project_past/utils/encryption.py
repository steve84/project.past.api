import hmac


def get_signature(secret: str, req_params: dict):
    """
    :param secret    : str, your api-secret
    :param req_params: dict, your request params
    :return: signature
    """
    _val = '&'.join([str(k)+"="+str(v) for k, v in sorted(req_params.items()) if (k != 'sign') and (v is not None)])
    return str(hmac.new(bytes(secret, "utf-8"), bytes(_val, "utf-8"), digestmod="sha256").hexdigest())