def to_number(digits):
    return int("".join(list(map(str, digits))))
    #return int("".join([str(d) for d in digits]))

print(to_number([21,2,33]))