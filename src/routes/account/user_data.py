"""
Api routes for searching professionals
"""
from flask import request

from routes.account.utils import requires_auth
from utils import proxy
from wsgi import app

prefix = "/api/users"


@app.route(prefix + '/create_note/', methods=["POST"])
@requires_auth
def create_note(**kwargs):
    user_key_dict = {"user_key": kwargs.get("user_key")}
    data = {**request.json, **user_key_dict}
    return proxy(data=data)

