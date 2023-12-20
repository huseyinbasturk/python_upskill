"""
9. Create a python file named custom_class_practices:
        9.1 Create a custom class named Pizza:
        Attributes:
            size, numberOfCheeseTopping, numberOfPepperoniTopping

            Add a constructor that can set all the fields

        Actions:
            calcCost(): returns the totalCost of the pizza
            __str__():returns a String containing the pizza size, quantity of each topping, and the pizza cost as calculated by calcCost()

        Pizza cost is determined by:
                        S: $10 + $2 per topping
                        M: $12 + $2 per topping
                        L: $14 + $2 per topping



        9.2 Create a class named Circle:
                Attributes:
                    instance: radius
                    static: pi

                Add a constructor that can set All the fields (instances)

                Actions:
                    calcArea(): returns the area of Circle

                    calcPerimeter(): returns the perimeter of Circle

                    __str__(): displays the radius, diameter, pi, area and perimeter of the circle when the object of circle is passed in the print statemen


"""


class Pizza:
    def __init__(self, size, numberOfCheeseTopping, numberOfPepperoniTopping):
        self.size = size
        self.numberOfCheeseTopping = numberOfCheeseTopping
        self.numberOfPepperoniTopping = numberOfPepperoniTopping

    def calc_cost(self):
        base_cost = {"S": 10, "M": 12, "L": 14}
        return base_cost.get(self.size, 0) + 2 * (self.numberOfCheeseTopping + self.numberOfPepperoniTopping)

    def __str__(self):
        return f"Size: {self.size}, Cheese Toppings: {self.numberOfCheeseTopping}, Pepperoni Toppings: {self.numberOfPepperoniTopping}, Cost: ${self.calc_cost()}"


pizza = Pizza("M", 3, 2)
print(pizza)


class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius


    def calc_area(self):
        return self.pi * self.radius ** 2


    def calc_perimeter(self):
        return 2 * self.pi * self.radius

    def __str__(self):
        return f"Radius: {self.radius}, Diameter: {self.radius * 2}, Pi: {self.pi}, Area: {self.calc_area()}, Perimeter: {self.calc_perimeter()}"



circle = Circle(5)
print(circle)