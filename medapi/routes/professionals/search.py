"""
Api routes for searching professionals
"""
from flask import request

from medapi.routes.account.utils import requires_auth, optional_auth
from medapi.utils import proxy
from medapi.wsgi import app

prefix = "/api/professionals"


@app.route(prefix + '/list_professionals/', methods=["GET"])
@optional_auth
def list_professionals(**kwargs):
    user_key_dict = {"user_key": kwargs.get("user_key")}
    params = {**request.args, **user_key_dict}
    return proxy(params=params)


@app.route(prefix + '/list_profession_types/', methods=["GET"])
def list_profession_types():
    return proxy()


@app.route(prefix + '/hi_there/', methods=["GET"])
def hi_there():
    return "Hi There"
