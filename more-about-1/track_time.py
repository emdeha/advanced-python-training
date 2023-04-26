import time

from typing import Callable, Any

def track_time(fn: Callable[[Any], Any]):
  def decorated_fn():
    start: float = time.perf_counter()
    fn()
    end: float = time.perf_counter()
    print(f'Elapsed time = {1000*(end - start):.3f}ms')
  return decorated_fn

@track_time
def sleep_long():
  time.sleep(2)

sleep_long()