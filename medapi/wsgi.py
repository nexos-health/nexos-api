from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api": {"origins": "*"}})


@app.route('/', methods=["GET"])
def hello():
    return "Hello, what are you doing here?"


if __name__ == "__main__":
    app.run()

from medapi.routes.payments.payments import *
from medapi.routes.authentication.account import *
from medapi.routes.professionals.groups import *
from medapi.routes.professionals.search import *

