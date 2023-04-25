from typing import Iterable

from wsgi.types import Environ, StartResponse
from .usecase import showStats

def ticker_endpoint(environ: Environ, start_response: StartResponse) -> Iterable[bytes]:
  symbol = environ['PATH_INFO'].split('/')[2]

  (open, financialCurrency) = showStats(symbol)

  start_response('200 OK', [('Content-Type', 'text/plain')])
  return [str.encode(f'Price for {symbol} - {open} {financialCurrency}')]