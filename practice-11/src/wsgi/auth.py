from wsgiref.headers import Headers

from typing import Iterable, Any
from .types import Environ, StartResponse

class APIKeyAuthenticationMiddleware:
  API_KEY_HEADER = 'X-APIKey'
  
  def __init__(self, app, apiKey):
    self.app = app
    self.headers = []
    self.apiKey = apiKey

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
    return self.API_KEY_HEADER in self.headers and self.headers[self.API_KEY_HEADER] == self.apiKey