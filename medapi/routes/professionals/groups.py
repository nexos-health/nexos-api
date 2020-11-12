"""
Api routes for searching professionals
"""
from flask import request

from routes.account.utils import requires_auth
from utils import proxy
from wsgi import app

prefix = "/api/groups"


@app.route(prefix + '/', methods=["GET"])
@requires_auth
def get_groups(**kwargs):
    params = {"user_key": kwargs.get("user_key")}
    return proxy(params=params)


@app.route(prefix + '/get_favourites/', methods=["GET"])
@requires_auth
def get_favourites(**kwargs):
    params = {"user_key": kwargs.get("user_key")}
    return proxy(params=params)


@app.route(prefix + '/', methods=["POST"])
@requires_auth
def create_group(**kwargs):
    user_key_dict = {"user_key": kwargs.get("user_key")}
    data = {**request.json, **user_key_dict}
    return proxy(data=data)


@app.route(prefix + '/edit_group/', methods=["PUT"])
@requires_auth
def edit_group(**kwargs):
    user_key_dict = {"user_key": kwargs.get("user_key")}
    data = {**request.json, **user_key_dict}
    return proxy(data=data)


@app.route(prefix + '/delete_group/', methods=["DELETE"])
@requires_auth
def delete_group(**kwargs):
    user_key_dict = {"user_key": kwargs.get("user_key")}
    data = {**request.json, **user_key_dict}
    return proxy(data=data)


@app.route(prefix + '/<id>/', methods=["GET"])
@requires_auth
def get_group(id, **kwargs):
    return proxy()


@app.route(prefix + '/add_professionals/', methods=["POST"])
@requires_auth
def add_professionals(**kwargs):
    user_key_dict = {"user_key": kwargs.get("user_key")}
    data = {**request.json, **user_key_dict}
    return proxy(data=data)


@app.route(prefix + '/remove_professionals/', methods=["DELETE"])
@requires_auth
def remove_professionals(**kwargs):
    user_key_dict = {"user_key": kwargs.get("user_key")}
    data = {**request.json, **user_key_dict}
    return proxy(data=data)
