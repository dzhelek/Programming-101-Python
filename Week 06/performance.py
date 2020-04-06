import time


def performance(file):
    def inner(func):

        def function():
            t1 = time.time()
            func()
            t2 = time.time()

            with open(file, 'a') as f:
                f.write(f"{func.__name__} was called\
 and took {t2 - t1} seconds to complete\n")

        return function
    return inner

# TypeError: Argument "name" of say_hello is not str!


def main():
    FILE = 'log.txt'
    with open(FILE, 'w') as f:
        f.write('')

    @performance(FILE)
    def something_heavy():
        time.sleep(2)
        return "I am done!"

    something_heavy()
    something_heavy()


if __name__ == '__main__':
    main()
