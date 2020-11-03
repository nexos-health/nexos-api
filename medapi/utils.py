from flask import request, Response, g
import requests

from medapi.settings import PEEPS_HOST


def proxy(
    host_url=PEEPS_HOST,
    headers=None,
    params=None,
    data=None,
    path=None,
    method=None,
    cookies=None,
):
    if not headers:
        headers = {key: value for (key, value) in request.headers if key != 'Host'}
    if not path:
        path = request.path
    if not method:
        method = request.method
    if not params:
        params = request.args or {}
    if not data:
        data = request.get_data() or {}
    if not cookies:
        cookies = request.cookies or {}

    resp = requests.request(
        method=method,
        url=host_url.strip("/") + path,
        headers=headers,
        params=params,
        json=data,
        cookies=cookies,
        allow_redirects=False
    )

    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    response_headers = [
        (name, value) for (name, value) in resp.raw.headers.items()
        if name.lower() not in excluded_headers
    ]

    response = Response(resp.content, resp.status_code, response_headers)
    return response
