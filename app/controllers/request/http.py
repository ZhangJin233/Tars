from flask import Blueprint
from flask import jsonify
from flask import request

from app.middleware.http_client import Request

req = Blueprint("request", __name__, url_prefix="/request")

@req.route('/http', methods=['POST'])
def http_request():
    data = request.get_json()
    method = data.get('method')
    if not method:
        return jsonify(dict(code=401, msg= 'method is required'))
    url = data.get('url')
    if not url:
        return jsonify(dict(code=401, msg= 'url is required'))  
    body = data.get('body')
    headers = data.get('header')
    r = Request(url, data=body, headers=headers)
    response = r.request(method)
    return jsonify(dict(code=200, data=response, msg='success'))