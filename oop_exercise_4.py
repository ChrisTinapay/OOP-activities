import math

class Fraction:
    def __init__(self, numerator, denominator):
        # Initialize the numerator and denominator properties
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator

    def add(self, other):
        # Add the current fraction and the other fraction
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        # Return the result as a new Fraction Object
        return Fraction(new_numerator, new_denominator)

    def subtract(self, other):
        # Subtract the other fraction from the current fraction
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        # Return the result as a new Fraction Object
        return Fraction(new_numerator, new_denominator)

    def multiply(self, other):
        # Multiply the current fraction and the other fraction
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        # Return the result as a new Fraction Object
        return Fraction(new_numerator, new_denominator)

    def divide(self, other):
        # Divide the current fraction by the other fraction
        if other.numerator == 0:
            raise ValueError("Cannot divide by a fraction with a numerator of 0")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        # Return the result as a new Fraction Object
        return Fraction(new_numerator, new_denominator)

    def simplify(self):
        # Simplify the current fraction to its simplest form
        gcd = math.gcd(self.numerator, self.denominator)
        # Return a new Fraction object with the simplified numerator and denominator
        return Fraction(self.numerator // gcd, self.denominator // gcd)

    def __str__(self):
         # Return the string representation of the fraction in the format "numerator/denominator"
        return f"{self.numerator}/{self.denominator}"


# Test your implementation
fraction1 = Fraction(1, 4)
fraction2 = Fraction(1, 2)

fraction3 = fraction1.add(fraction2)
print(fraction3)  # Should output "6/8"

fraction4 = fraction3.simplify()
print(fraction4)  # Should output "3/4"
