from flask.views import MethodView

from .usecase import run
from myflask.auth import auth_api_key

class TickerAPI(MethodView):
  decorators=[auth_api_key]

  def post(self, symbol: str) -> str:
    (open, financialCurrency) = run(symbol)

    return f'Price for {symbol} - {open} {financialCurrency}'