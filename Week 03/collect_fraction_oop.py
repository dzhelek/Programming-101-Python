from simplify_fractions_oop import simplify_fraction, Fraction


class Fraction(Fraction):
    def __add__(self, other):
        pass


def common_denominator(fractions):
    denominators = [fraction.denominator for fraction in fractions]
    min_denominator = min(denominators)
    counter = 1
    common = min_denominator
    for i in range(len(denominators) - 1):
        while common % denominators[i] != 0 or common % denominators[i + 1] != 0:
            common = min_denominator * counter
            counter += 1
    for fraction in fractions:
        if fraction.denominator != common:
            fraction.nominator *= common // fraction.denominator
            fraction.denominator *= common // fraction.denominator


def common_denominator(fractions):
    denominators = [fraction[1] for fraction in fractions]
    min_denominator = min(denominators)
    counter = 1
    common = min_denominator
    for i in range(len(denominators) - 1):
        while common % denominators[i] != 0 or common % denominators[i+1] != 0:
            common = min_denominator * counter
            counter += 1
    for fraction in fractions:
        if fraction[1] != common:
            fraction[0] *= common // fraction[1]
            fraction[1] *= common // fraction[1]
    return fractions


def collect_fractions(fractions):
    fractions =\
     [Fraction(fraction.nominator, fraction.denominator) for fraction in fractions]

    for fraction in fractions:
        fraction.simplify_fractions()

    common_denominator(fractions)

    return sum(fractions)


def collect_fractions(fractions):
    fractions = [list(simplify_fraction(i)) for i in fractions]
    fractions = common_denominator(fractions)
    nominators_sum = sum(fraction[0] for fraction in fractions)
    collected = (nominators_sum, fractions[0][1])
    return simplify_fraction(collected)


def main():
    print(collect_fractions([(1,2), (4,5), (-4, 10)]))


if __name__ == '__main__':
    main()
