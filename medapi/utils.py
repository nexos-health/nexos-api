from flask import request, Response
import requests


def proxy_request(*args, **kwargs):
    resp = requests.request(
        method=request.method,
        url=request.url.replace(request.host_url, 'new-domain.com'),
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False)

    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
               if name.lower() not in excluded_headers]

    response = Response(resp.content, resp.status_code, headers)
    return response
