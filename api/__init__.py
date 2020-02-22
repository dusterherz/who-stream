from flask import Flask
from flask_restx import Api

from .is_live import api as is_live_api

app = Flask(__name__)

api = Api(app, title="Who stream API",
          version="0.1",
          description="The API to answer to Google Home for Who Stream")

api.add_namespace(is_live_api)
