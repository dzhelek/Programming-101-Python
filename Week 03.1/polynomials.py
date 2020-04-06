import sys


class Term:
    def __init__(self, term):
        pass


def check(polynomial):
    polynomial = polynomial.split('+')
    i = 0
    while True:
        try:
            int(polynomial[i][0])
        except ValueError:
            integer = polynomial[i][0]
            break
        else:
            try:
                integer = polynomial[i][1]
            except IndexError:
                i += 1
            else:
                break

    count = 0
    for monomial in polynomial:
        if integer not in monomial:
            count += 1
    assert count <= 1, "invalid input!"
    return True


def get_derivative(polynomial):
    polynomial = polynomial.split('+')
    polynomial = [Term(term) for term in polynomial]
    for term in polynomial:
        term.derivative()
    return polynomial


def main():
    print(get_derivative(sys.argv[1]))


if __name__ == '__main__':
    main()
