# Fraction class from
# http://interactivepython.org/runestone/static/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html
# To make sure you understand how operators are implemented in Python classes,
# and how to properly write methods, write some methods to implement *, /, and -
# Also implement comparison operators > and <

# Other optomizations:
# DONE 1. Implement the simple methods getNum and getDen that will return the numerator
# and denominator of a fraction.

# DONE 2. In many ways it would be better if all fractions were maintained in lowest
# terms right from the start. Modify the constructor for the Fraction class so
# that GCD is used to reduce fractions immediately. Notice that this means the
# __add__ function no longer needs to reduce. Make the necessary modifications.

# DONE 3. Implement the remaining relational operators (__ge__, __le__, and __ne__)

# DONE 4. Modify the constructor for the fraction class so that it checks to make
# sure that the numerator and denominator are both integers. If either is not an
# integer the constructor should raise an exception.

# DONE 5. In the definition of fractions we assumed that negative fractions have a
# negative numerator and a positive denominator. Using a negative denominator
# would cause some of the relational operators to give incorrect results. In
# general, this is an unnecessary constraint. Modify the constructor to allow
# the user to pass a negative denominator so that all of the operators continue
# to work properly.

# DONE 6. Research the __radd__ method. How does it differ from __add__? When is it
# used? Implement __radd__.
#
#   __radd__ is reverse add, it is used to add the self to the other as opposed
#   to the other to self.  It is useful if the other that self would be added to
#   (the left operand) doesn't have an add function, so we can use the reverse add
#   on the other one.  As addition is commutative, the implemention of __radd__
#   in this case does not need to be different than __add__.

# DONE 7. Repeat the last question but this time consider the __iadd__ method.
#
#   __iadd__ should attempt to modify the object IN PLACE instead of creating a
#   new object with the incremented value (as our __add__ function does.)  This
#   __iadd__ function will be called, for example, in a loop with a "+="

# DONE 8. Research the __repr__ method. How does it differ from __str__? When is it
# used? Implement __repr__.
#
#   __str__ is meant to be readable - itcan be somewhat vague and doesn't have
#   to be a valid python expression.  __repr__ is used for debugging and should
#   contain all the information one would need to recreate an object with the same
#   value.


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
        if top % 1 > 0 or bottom % 1 > 0:
            raise ValueError("both the numerator and denominator must be whole numbers")
        if bottom < 0:
            top = 0 - top
            bottom = abs(bottom)
        common = gcd(top, bottom)
        self.num = int(top//common)
        self.den = int(bottom//common)

    def __str__(self):
        if self.num == self.den:
            return "1"
        return str(self.num)+"/"+str(self.den)

    def __repr__(self):
        return "Fraction(%r, %r)" %(self.num, self.den)

    def get_num(self):
        """return numerator"""
        return self.num

    def get_den(self):
        """return the denominator"""
        return self.den

    def show(self):
        print(self.num, "/", self.den)

    def __add__(self, otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)

    def __radd__(self, other):
        """addition is commutative, as is multiplication"""
        if other.__class__ == Fraction:
            return self.__add__(other)
        else:
            other = Fraction(other, 1)
            return self.__add__(other)

    def __iadd__(self, other):
        """perform addition in place"""
        if other.__class__ != Fraction:
            other = Fraction(other, 1)
        new_num = self.num*other.den + self.den*other.num
        new_den = self.den*other.den
        common = gcd(new_num, new_den)
        self.num = new_num // common
        self.den = new_den // common
        return self

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

    def __le__(self, other):
        """less than or eauql to"""
        numerator1 = self.num * other.den
        numerator2 = other.num * self.den
        if numerator1 <= numerator2:
            return True
        return False

    def __gt__(self, other):
        """greater than"""
        numerator1 = self.num * other.den
        numerator2 = other.num * self.den
        if numerator1 > numerator2:
            return True
        return False

    def __ge__(self, other):
        """greater than or equal to"""
        numerator1 = self.num * other.den
        numerator2 = other.num * self.den
        if numerator1 >= numerator2:
            return True
        return False

    def __ne__(self, other):
        numerator1 = self.num * other.den
        numerator2 = other.num * self.den
        if numerator1 == numerator2:
            return False
        return True

    def __sub__(self, other):
        """subtraction"""
        numerator1 = self.num * other.den
        numerator2 = other.num * self.den
        final_num = numerator1 - numerator2
        final_den = other.den * self.den
        return Fraction(final_num, final_den)

    def __mul__(self, other):
        """multiplication"""
        numerator = self.num * other.num
        denom = self.den * other.den
        return Fraction(numerator, denom)

    def __div__(self, other):
        """division

        division of two fractions is the same as multiplying by the reciprocal"""
        numerator = self.num * other.den
        denom = self.den * other.num
        return Fraction(numerator, denom)


x = Fraction(1, 2)
y = Fraction(2, 3)
print(x + y)
print(x == y)
