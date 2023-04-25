from flask.views import MethodView
from flask import request

from myflask.auth import auth_api_key
from .usecase import saveTickerList

class TickerListAPI(MethodView):
  decorators=[auth_api_key]

  def post(self) -> str:
    parsed = str(request.query_string).split('=')[1]
    tickers = parsed.split(',')
    saveTickerList(tickers)
    return ''