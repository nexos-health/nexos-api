"""
Api routes for searching professionals
"""
from flask import request

from medapi.routes.authentication.utils import requires_auth
from medapi.utils import proxy
from medapi.wsgi import app

prefix = "/api/professionals"


@app.route(prefix + '/list_professionals/', methods=["GET"])
def list_professionals():
    return proxy()


