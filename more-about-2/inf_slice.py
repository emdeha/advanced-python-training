from typing import List
from itertools import count, islice

def inf_slice(a: int, b: int) -> List[int]:
  return islice(count(0), a, b)

for elem in inf_slice(10, 15):
  print(elem)