"""
Api routes for searching professionals
"""
from flask import request

from medapi.utils import proxy_request
from medapi.wsgi import app

prefix = "/api/professionals"


@app.route(prefix + '/list_professionals/', methods=["GET"])
def list_professionals():
    return proxy_request(request)


@app.route(prefix + '/list_profession_types/', methods=["GET"])
def list_profession_types():
    return proxy_request(request)
