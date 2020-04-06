def simplify_positive_fraction(fraction):
    if fraction[0] == 0:
        return (0, 1)

    for i in range(2, min(fraction) + 1):
        if fraction[0] % i == fraction[1] % i == 0:
            fraction = [j // i for j in fraction]
            i -= 1
    return tuple(fraction)


def simplify_fraction(fraction):
    assert fraction[1] != 0, "Denominator cannot be equal to zero!"

    fraction = list(fraction)

    while fraction[0] != int(fraction[0]) or fraction[1] != int(fraction[1]):
        fraction[0] *= 10
        fraction[1] *= 10

    fraction[0] = int(fraction[0])
    fraction[1] = int(fraction[1])

    positive = simplify_positive_fraction(tuple(map(abs, fraction)))
    if (fraction[0] < 0) ^ (fraction[1] < 0):
        return((-positive[0], positive[1]))
    else:
        return positive


def main():
    print(simplify_fraction((2.5, 0.5)))


if __name__ == '__main__':
    main()