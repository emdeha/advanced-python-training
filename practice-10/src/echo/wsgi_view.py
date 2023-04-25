from typing import Iterable

from wsgi.types import Environ, StartResponse
from .usecase import run

def echo_endpoint(environ: Environ, start_response: StartResponse) -> Iterable[bytes]:
  try:
    request_body_size = int(environ.get('CONTENT_LENGTH', 0))
  except ValueError:
    request_body_size = 0
  
  request_body = environ['wsgi.input'].read(request_body_size)

  start_response('200 OK', [('Content-Type', 'text/plain')])
  return [run(request_body)]