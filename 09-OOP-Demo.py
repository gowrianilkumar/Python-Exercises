class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """The radius property."""
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def diameter(self):
        """The diameter property."""
        return self._radius * 2

    @property
    def area(self):
        """The area property."""
        return 3.14159 * (self._radius ** 2)

# Example usage:
circle = Circle(5)
print(f"Radius: {circle.radius}")
print(f"Diameter: {circle.diameter}")
print(f"Area: {circle.area}")

# Update the radius
circle.radius = 10
print(f"Updated Radius: {circle.radius}")
print(f"Updated Diameter: {circle.diameter}")
print(f"Updated Area: {circle.area}")

# Attempt to set a negative radius (will raise ValueError)
try:
    circle.radius = -3
except ValueError as e:
    print(e)
