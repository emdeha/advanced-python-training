from .usecase import run
from myflask.auth import auth_api_key

@auth_api_key
def ticker_view(symbol: str) -> str:
  (open, financialCurrency) = run(symbol)

  return f'Price for {symbol} - {open} {financialCurrency}'