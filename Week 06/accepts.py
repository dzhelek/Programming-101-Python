def accepts(*types):
    def inner(func):
        def function(*args):
            for i in range(len(args)):
                if type(args[i]) != types[i]:
                    raise TypeError(f"Argument {func.__code__.co_varnames[i]}\
 of {func.__name__} is not {types[i].__name__}")
        return function
    return inner

# TypeError: Argument "name" of say_hello is not str!


def main():
    @accepts(str, int)
    def deposit(name, money):
        print("{} sends {} $!".format(name, money))

    deposit("Marto", "Marto")


if __name__ == '__main__':
    main()
