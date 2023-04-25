from typing import Iterable
from .types import Environ, StartResponse

def not_found(_: Environ, start_response: StartResponse) -> Iterable[bytes]:
  start_response('404 Not Found', [])
  return []