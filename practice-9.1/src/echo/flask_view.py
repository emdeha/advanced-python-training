from flask import request
from flask.views import MethodView

from .usecase import run
from myflask.auth import auth_api_key

class EchoAPI(MethodView):
  decorators=[auth_api_key]

  def post(self) -> bytes:
    return run(request.get_data())