"""
Api routes for searching professionals
"""
from flask import request

from medapi.routes.authentication.utils import requires_auth
from medapi.utils import proxy
from medapi.wsgi import app

prefix = "/api/groups"


@app.route(prefix + '/', methods=["GET"])
@requires_auth
def get_groups(**kwargs):
    # params = {"user_key": kwargs.get("user_key")}
    params = {"user_key": "UK4BSGB9"}
    return proxy(params=params)


@app.route(prefix + '/', methods=["POST"])
@requires_auth
def create_group(**kwargs):
    # user_key_dict = {"user_key": kwargs.get("user_key")}
    user_key_dict = {"user_key": "UK4BSGB9"}
    data = {**request.json, **user_key_dict}
    return proxy(data=data)


@app.route(prefix + '/<id>/', methods=["GET"])
@requires_auth
def get_group(id, **kwargs):
    return proxy()


@app.route(prefix + '/add_professional/', methods=["POST"])
@requires_auth
def add_professional(**kwargs):
    # user_key_dict = {"user_key": kwargs.get("user_key")}
    user_key_dict = {"user_key": "UK4BSGB9"}
    data = {**request.data, **user_key_dict}
    return proxy(data=data)


@app.route(prefix + '/remove_professional/', methods=["DELETE"])
@requires_auth
def remove_professional(**kwargs):
    # user_key_dict = {"user_key": kwargs.get("user_key")}
    user_key_dict = {"user_key": "UK4BSGB9"}
    data = {**request.data, **user_key_dict}
    return proxy(data=data)
