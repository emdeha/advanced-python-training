from wsgiref.simple_server import make_server
from wsgiref.headers import Headers
from typing import Iterable, Any

from echo.wsgi_view import echo_endpoint
from ticker.wsgi_view import ticker_endpoint
from wsgi.notfound import not_found
from wsgi.types import Environ, StartResponse
from wsgi.auth import APIKeyAuthenticationMiddleware

def trading_wsgi_app(environ: Environ, start_response: StartResponse) -> Iterable[bytes]:
  path = environ['PATH_INFO']
  if path == '/':
    return echo_endpoint(environ, start_response)
  if path.startswith('/ticker'):
    return ticker_endpoint(environ, start_response)
  else:
    return not_found(environ, start_response)

def serve(host, port, apiKey):
  server = make_server(host, port, APIKeyAuthenticationMiddleware(trading_wsgi_app, apiKey))
  server.serve_forever()