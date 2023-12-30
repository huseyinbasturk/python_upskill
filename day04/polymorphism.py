from day03.abstraction2 import Shape, Square, Rectangle
from day03.encapsulations1 import Person

shape1: Shape = Square(5)

shape2: Shape = Rectangle(3,4)

def display_area(shape: Shape):  # parameter's type is restricted to shape objects only
    print(f"the {shape.name}\' area is {shape.area()}")

display_area(shape1)
display_area(shape2)


person = Person('Quaresma', 40)
# display_area(person)



