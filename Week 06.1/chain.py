def chain(lst1, lst2):
    for item in lst1:
        yield item
    for item in lst2:
        yield item
