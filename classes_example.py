# Classes Example

# Create some classes and objects
import math


class Shape:
    """Represents a 2-dimensional polygon

    Attributes:
        num_sides: An integer count of the sides
        side_length: A float of side length
    """

    def __init__(self):
        """Creates a new shape with default values."""
        self.num_sides = 4
        self.side_length = 10.0

    def area(self) -> float:
        """Return the area of a square."""
        return self.side_length ** 2

    def perimter(self) -> float:
        return self.side_length * 4

# TODO: do this on your own


# TODO: call the function and print out the results

class Circle(Shape):


    def __init__(self, radius: float = 5):

        super().__init__()

        self.radius = radius

def area(self) -> float:

    return math.pi * self.radius ** 2

some_shape = Shape()
print(some_shape.area())
print(some_shape.perimter())


some_circle = Circle(10)
print(some_circle.area())
print(some_circle.radius())
print(some_circle.num_sides)
