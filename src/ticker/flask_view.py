from flask.views import MethodView

from .usecase import run
from myflask.auth import auth_api_key
from tasks.show_message import show_message

class TickerAPI(MethodView):
  decorators=[auth_api_key]

  def post(self, symbol: str) -> str:
    (open, financialCurrency) = run(symbol)

    if 'VMW' == symbol:
      # mypy complains that delay isn't defined for some reason, so we ignore it
      show_message.delay(symbol) # type: ignore[attr-defined]

    return f'Price for {symbol} - {open} {financialCurrency}'