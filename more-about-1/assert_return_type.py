from typing import Callable, Any, Type

def returns(rtype: Type):
  def check_returns(fn: Callable[[Any], Any]):
    def new_f(*args: Any, **kwds: Any):
      result = fn(*args, **kwds)
      assert isinstance(result, rtype), \
        f'return value {result} does not match {rtype}'
      return result
    new_f.__name__ = fn.__name__
    return new_f
  return check_returns

@returns(str)
def func(arg1: int, arg2: int):
  return arg1 * arg2

func(1, 2)