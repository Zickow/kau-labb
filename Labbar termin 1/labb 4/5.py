import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getradius(self):
        return self.radius

    def setRadius(self, new_radius):
        self.radius = new_radius

    def area(self):
        return math.pi * self.radius * self.radius

    def circumference(self):
        return 2 * math.pi * self.radius


r = float(input("Enter radius: "))
c = Circle(r)

print("Area:", c.area())
print("Circumferecnce:", c.circumference())