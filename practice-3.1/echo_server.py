from wsgiref.simple_server import make_server

def echo_wsgi_app(environ, start_response):
  try:
    request_body_size = int(environ.get('CONTENT_LENGTH', 0))
  except ValueError:
    request_body_size = 0
  
  request_body = environ['wsgi.input'].read(request_body_size)

  start_response('200 OK', [('Content-Type', 'text/plain')])
  return [request_body]

if __name__ == "__main__":
  server = make_server('localhost', 1337, echo_wsgi_app)
  server.serve_forever()
