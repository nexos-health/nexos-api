import requests
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv, find_dotenv
from flask import jsonify, request
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for
from flask_cors import cross_origin
from functools import wraps
import logging
import json
from os import environ as env
from six.moves.urllib.parse import urlencode
from werkzeug.exceptions import HTTPException

import settings
from wsgi import app

logger = logging.getLogger(__name__)
oauth = OAuth(app)

auth0 = oauth.register(
    'auth0',
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    api_base_url=f"https://{settings.AUTH0_DOMAIN}",
    access_token_url=f"https://{settings.AUTH0_DOMAIN}/oauth/token",
    authorize_url=f"https://{settings.AUTH0_DOMAIN}/authorize",
    client_kwargs={
        'scope': 'openid profile email',
    },
)

prefix = "/api/account"


@app.route(prefix + '/signup', methods=["POST"])
def signup():
    """
    Creates new user during signup
    Args:
        email:

    Returns:

    """
    json_body = request.json
    create_user_url = settings.PEEPS_HOST + "/api/users/"
    create_favourites_group_url = settings.PEEPS_HOST + "/api/groups/create_favourites_group/"
    try:
        resp = requests.post(create_user_url, data={"email": json_body["email"], "auth_id": json_body["auth_id"]})
        user_key = resp.json()["user_key"]
        logger.info(f"User Key: {user_key}")
        favourites_resp = requests.post(create_favourites_group_url, data={"user_key": user_key})
        logger.info(f"Favourites Response: {favourites_resp.status_code} - {favourites_resp.text}")
        if favourites_resp.status_code != 201:
            raise Exception
    except Exception as ex:
        return jsonify(data=f"Error: {ex}"), 500

    data = {"user_key": user_key}
    return jsonify(data)
