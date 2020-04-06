class Fraction():
    def __init__(self, nominator, denominator):
        self.nominator = nominator
        self.denominator = denominator


    def min(self):
        return min(self.nominator, self.denominator)


    def abs(self):
        self.nominator = abs(self.nominator)
        self.denominator = abs(self.denominator)


    def _simplify_positive_fraction(self):
        if self.nominator == 0:
            self.nominator = 0
            self.denominator = 1

        for i in range(2, self.min() + 1):
            if self.nominator % i == self.denominator % i == 0:
                self.nominator = self.nominator // i
                self.denominator = self.denominator // i
                i -= 1


    def simplify_fraction(self):
        assert self.denominator != 0, "Denominator cannot be equal to zero!"

        while self.nominator != int(self.nominator) or\
         self.denominator != int(self.denominator):
            self.nominator *= 10
            self.denominator *= 10

        self.nominator = int(self.nominator)
        self.denominator = int(self.denominator)

        if (self.nominator < 0) ^ (self.denominator < 0):
            self.nominator = -self.nominator
            self._simplify_positive_fraction()
            self.nominator = -self.nominator
        else:
            self.abs()
            self._simplify_positive_fraction()


def simplify_fraction(fraction):
    f = Fraction(fraction[0], fraction[1])
    f.simplify_fraction()
    return (f.nominator, f.denominator)


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
