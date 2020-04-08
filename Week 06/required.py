import inspect

def required(func):
    print(inspect.unwrap(func).__qualname__)
    return func


def main():
    class Animal:
        @required
        def eat(self, food):
            pass

    class Panda(Animal):
        pass

    Panda()


if __name__ == '__main__':
    main()


# ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defau
# lts__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
#  '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '
# __init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module_
# _', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex_
# _', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

