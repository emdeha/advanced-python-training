class UpperAttrMetaclass(type):
  def __new__(cls, clsname, bases, attrs):
    uppercase_attrs = {
      attr if attr.startswith('__') else attr.upper(): v
      for attr, v in attrs.items()
    }

    return super().__new__(cls, clsname, bases, uppercase_attrs)

class Foo(object, metaclass=UpperAttrMetaclass):
  foo: int = 0
  bar: str = 'asdf'

foo = Foo()
print(foo.bar)