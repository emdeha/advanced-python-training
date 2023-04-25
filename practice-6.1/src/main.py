from wsgi.app import serve

if __name__ == '__main__':
  serve('localhost', 1337, apiKey='test123')