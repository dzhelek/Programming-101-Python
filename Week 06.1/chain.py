def chain(iterable_one, iterable_two):
    for item in iterable_one:
        yield item
    for item in iterable_two:
        yield item
