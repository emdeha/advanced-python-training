class Fibonacci():
  def __init__(self, limit: int):
    self.limit = limit
    self.current = 0
    self.next = 1

  def __iter__(self):
    return self

  def __next__(self) -> int:
    if self.next > self.limit:
      raise StopIteration

    result = self.current
    self.current, self.next = self.next, self.next + self.current
    return result

fib = iter(Fibonacci(3))
print(next(fib))
print(next(fib))
print(next(fib))

def fibonacci(limit: int) -> int:
  current: int = 0
  next: int = 1

  while True:
    if next > limit:
      raise StopIteration

    result = current
    current, next = next, next + current
    yield result
    
fib2 = iter(fibonacci(3))
print(next(fib2))
print(next(fib2))
print(next(fib2))
print(next(fib2))