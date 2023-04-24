from flask.views import MethodView
from flask import request
from sqlalchemy.engine import Engine

from myflask.auth import auth_api_key
from .usecase import save_ticker_list, get_stats

class MonitoredAPI(MethodView):
  decorators=[auth_api_key]

  def __init__(self, db: Engine) -> None:
    self.db = db

  def get(self) -> str:
    stats = get_stats(self.db)
    return '\n' + '; '.join(stats) + '\n'

  def post(self) -> str:
    parsed = str(request.query_string).strip("'").split('=')[1]
    tickers = parsed.split(',')
    save_ticker_list(self.db, tickers)
    return ''