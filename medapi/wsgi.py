from flask import Flask
from flask_cors import CORS
import logging

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}}, expose_headers="Content-Type")

logging_handler = logging.FileHandler(
    filename="./medplatform-api.log", encoding='utf-8', mode='a+'
)
logging.basicConfig(
    handlers=[logging_handler],
    format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
    datefmt="%F %A %T",
    level=logging.DEBUG
)

# cors = CORS(app)
logger = logging.getLogger(__name__)


@app.route('/', methods=["GET"])
def hello():
    logger.info("Hello there")
    return "Hello, what are you doing here?"


if __name__ == "__main__":
    app.run()

from medapi.routes.payments.payments import *
from medapi.routes.account.account import *
from medapi.routes.account.user_data import *
from medapi.routes.professionals.groups import *
from medapi.routes.professionals.search import *

