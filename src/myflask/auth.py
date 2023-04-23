from flask import request, make_response
from functools import wraps
from typing import Callable, Any

def auth_api_key(f: Callable):
  API_KEY_HEADER = 'X-APIKey'
  API_KEY = 'test123'

  @wraps(f)
  def decorator(*args, **kwargs) -> Any:
    if API_KEY_HEADER not in request.headers or request.headers[API_KEY_HEADER] != API_KEY:
      return make_response('Unauthorized', 401)
    return f(*args, **kwargs)
  return decorator