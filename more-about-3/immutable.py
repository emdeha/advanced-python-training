from typing import Any

class Immutable:
  def __setattr__(self, __name: str, __value: Any) -> None:
    pass

  def __delattr__(self, __name: str) -> None:
    pass

class Person(Immutable):
  def __init__(self, name: str, age: int):
    self.__dict__['name'] = name
    self.__dict__['age'] = age

  def __str__(self) -> str:
    return f'{self.name} {self.age}'

person = Person('Peter', 39)
print(person)
person.name = 'Ivan'
print(person)