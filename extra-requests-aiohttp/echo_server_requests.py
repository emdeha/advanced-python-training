from wsgiref.simple_server import make_server
from wsgiref.headers import Headers
import requests
import json
from typing import Dict, Iterable, Any, Callable

Environ = Dict[str, Any]
StartResponse = Callable[[str, Any], Any]

def trading_wsgi_app(environ: Environ, start_response: StartResponse) -> Iterable[bytes]:
  path = environ['PATH_INFO']
  if path == '/':
    return echo_endpoint(environ, start_response)
  if path.startswith('/ticker'):
    return ticker_endpoint(environ, start_response)
  else:
    return not_found(environ, start_response)

def not_found(environ: Environ, start_response: StartResponse) -> Iterable[bytes]:
  start_response('404 Not Found', [])
  return []

def echo_endpoint(environ: Environ, start_response: StartResponse) -> Iterable[bytes]:
  try:
    request_body_size = int(environ.get('CONTENT_LENGTH', 0))
  except ValueError:
    request_body_size = 0
  
  request_body = environ['wsgi.input'].read(request_body_size)

  start_response('200 OK', [('Content-Type', 'text/plain')])
  return [request_body]

def ticker_endpoint(environ: Environ, start_response: StartResponse) -> Iterable[bytes]:
  symbol = environ['PATH_INFO'].split('/')[2]

  response = requests.get(
    f'https://query2.finance.yahoo.com/v10/finance/quoteSummary/{symbol}?modules=financialData',
    headers={
      'User-Agent': '',
    },
  )
  content = response.json()

  quote = content['quoteSummary']['result'][0]['financialData']
  open = quote['currentPrice']['fmt']
  financialCurrency = quote['financialCurrency']

  start_response('200 OK', [('Content-Type', 'text/plain')])
  return [str.encode(f'Price for {symbol} - {open} {financialCurrency}')]

class APIKeyAuthenticationMiddleware:
  API_KEY = 'test123'
  API_KEY_HEADER = 'X-APIKey'
  
  def __init__(self, app):
    self.app = app
    self.headers = []

  def __call__(self, environ: Environ, start_response: StartResponse) -> Iterable[Any]:
    self.parse_headers(environ)

    if not self.is_authorized():
      start_response('401 Unauthorized', [])
      return []

    return self.app(environ, start_response)

  def parse_headers(self, environ: Environ) -> None:
    self.headers = Headers([])
    for k, v in environ.items():
      if 'HTTP' in k:
        key = k.replace('HTTP_', '').lower().replace('_', '-')
        self.headers[key] = v
  
  def is_authorized(self) -> bool:
    return self.API_KEY_HEADER in self.headers and self.headers[self.API_KEY_HEADER] == self.API_KEY

if __name__ == "__main__":
  server = make_server('localhost', 1337, APIKeyAuthenticationMiddleware(trading_wsgi_app))
  server.serve_forever()
