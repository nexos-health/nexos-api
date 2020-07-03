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


@app.route(prefix + '/<id>/', methods=["POST"])
@requires_auth
def create_group(group_id):
    return proxy(params={"id": group_id})


@app.route(prefix + '/<id>/', methods=["GET"])
@requires_auth
def get_group(id, **kwargs):
    return proxy()


@app.route(prefix + '/<id>/add_professional', methods=["PUT"])
@requires_auth
def add_professional(id):
    return proxy()


@app.route(prefix + '/<id>/remove_professional', methods=["PUT"])
@requires_auth
def remove_professional(id):
    return proxy()
