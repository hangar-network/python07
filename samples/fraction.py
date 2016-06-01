class Fraction:
    """ This class represents a fraction (rational number with numerator and
        denominator).
    """
    def __init__(self, num, den):
        self.numerator = num
        self.denominator = den


    def __add__(self, other):
        if(type(other) == type(1)):
            return self + Fraction(other, 1)
        else:
            num = self.numerator * other.denominator + other.numerator * self.denominator
            den = self.denominator * other.denominator
            result = Fraction(num, den)

        return Fraction.simplify(result)

    def __sub__(self, other):
        print(self.numerator, self.denominator)

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __floordiv__(self, other):
        pass

    def __repr__(self):
        return str(self)

    def __str__(self):
        representation = "{}/{}".format(self.numerator, self.denominator)
        return representation

    # def __eq__(self, outra):
    #     if self.numerador == outra.numerador
    #     and self.denominador == outra.denominador:
    #         return True
    #     else
    #         return False
    def __lt__(self, outra):
        if self.numerador <= outra.numerador:
            return True
        else:
            return False

    def __le__(self, outra):
        if self.numerador <= outra.numerador:
            return True
        else:
            return False

    def __gt__(self, outra):
        return not (self <= outra)

    # INSTANCE FUNCTION
    def simplify_immutable(self):
        mdc = math.gcd(self.numerator, self.denominator)
        num = self.numerator/mdc
        den = self.denominator/mdc
        res = Fraction(num, den)
        return res

    # CLASS FUCTION
    def simplify_immutable(fraction):
        mdc = math.gcd(fraction.numerator, fraction.denominator)
        num = fraction.numerator/mdc
        den = fraction.denominator/mdc
        return Fraction(num, den)

    # Mutable Approach
    def simplify_mutable(self):
        mdc = math.gcd(self.numerator, self.denominator)
        self.numerator = self.numerator/mdc
        self.denominator = self.denominator/mdc


if __name__ == '__main__':
    a = Fraction(2, 4)
    print(a)
    lista = [a]
    print(lista)

    a = a.simplify()
    #Fraction.simplify(a)
