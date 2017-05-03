# Fraction class from
# http://interactivepython.org/runestone/static/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html
# To make sure you understand how operators are implemented in Python classes,
# and how to properly write methods, write some methods to implement *, /, and -
# Also implement comparison operators > and <


def gcd(m, n):
    """Euclid's algorithm"""
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        if self.num == self.den:
            return "1"
        return str(self.num)+"/"+str(self.den)

    def __repr__(self):
        return self.__str__()

    def show(self):
        print(self.num, "/", self.den)

    def __add__(self, otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

    def __lt__(self, other):
        """less than"""
        numerator1 = self.num * other.den
        numerator2 = other.num * self.den
        if numerator1 < numerator2:
            return True
        return False

    def __gt__(self, other):
        """greater than"""
        numerator1 = self.num * other.den
        numerator2 = other.num * self.den
        if numerator1 > numerator2:
            return True
        return False

    def __sub__(self, other):
        """subtraction"""
        numerator1 = self.num * other.den
        numerator2 = other.num * self.den
        final_num = numerator1 - numerator2
        final_den = other.den * self.den
        common = gcd(final_num, final_den)
        return Fraction(final_num//common, final_den//common)

    def __mul__(self, other):
        """multiplication"""
        numerator = self.num * other.num
        denom = self.den * other.den
        common = gcd(numerator, denom)
        return Fraction(numerator//common, denom//common)

    def __div__(self, other):
        """division

        division of two fractions is the same as multiplying by the reciprocal"""
        numerator = self.num * other.den
        denom = self.den * other.num
        common = gcd(numerator, denom)
        return Fraction(numerator//common, denom//common)


x = Fraction(1, 2)
y = Fraction(2, 3)
print(x + y)
print(x == y)
