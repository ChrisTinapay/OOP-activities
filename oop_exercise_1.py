# SIMPLE CLASS
import math

class Circle:
 def __init__(self, radius):
     # Initialize the radius property
     self.radius = radius

 def area(self):
     # Calculate and return the area of the circle
     return math.pi * self.radius**2


 def circumference(self):
     # Calculate and return the circumference of the circle
     return 2 * self.radius * math.pi
    

 def diameter(self):
     # Calculate and return the diameter of the circle
     return 2 * self.radius
    

# Test your implementation
circle1 = Circle(3)
print(circle1.area())  # Should output approximately 28.274333882308138
print(circle1.circumference())  # Should output approximately 18.84955592153876
print(circle1.diameter())  # Should output 6

circle2 = Circle(5)
print(circle2.area())  # Should output approximately 78.53981633974483
print(circle2.circumference())  # Should output approximately 31.41592653589793
print(circle2.diameter())  # Should output 10
