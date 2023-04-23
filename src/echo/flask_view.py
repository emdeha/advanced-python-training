from flask import request

from .usecase import run
from myflask.auth import auth_api_key

@auth_api_key
def echo_view() -> bytes:
  return run(request.get_data())