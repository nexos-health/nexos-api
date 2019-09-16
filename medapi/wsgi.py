from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api": {"origins": "*"}})

from medapi.routes.payments.payments import *

if __name__ == "__main__":
    app.run()