from wsgiref.simple_server import make_server
from wsgiref.headers import Headers

def echo_wsgi_app(environ, start_response):
  try:
    request_body_size = int(environ.get('CONTENT_LENGTH', 0))
  except ValueError:
    request_body_size = 0
  
  request_body = environ['wsgi.input'].read(request_body_size)

  start_response('200 OK', [('Content-Type', 'text/plain')])
  return [request_body]

class APIKeyAuthenticationMiddleware:
  API_KEY = 'test123'
  API_KEY_HEADER = 'X-APIKey'
  
  def __init__(self, app):
    self.app = app
    self.headers = []

  def __call__(self, environ, start_response):
    self.parse_headers(environ)

    if not self.is_authorized():
      start_response('401 Unauthorized', [])
      return []

    return self.app(environ, start_response)

  def parse_headers(self, environ):
    self.headers = Headers([])
    for k, v in environ.items():
      if 'HTTP' in k:
        key = k.replace('HTTP_', '').lower().replace('_', '-')
        self.headers[key] = v
  
  def is_authorized(self):
    return self.API_KEY_HEADER in self.headers and self.headers[self.API_KEY_HEADER] == self.API_KEY

if __name__ == "__main__":
  server = make_server('localhost', 1337, APIKeyAuthenticationMiddleware(echo_wsgi_app))
  server.serve_forever()