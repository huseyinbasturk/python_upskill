"""
2. Create a python file named encapsulation_practice:
		create a class called Item
		    private variables:
		        name, unit_price, quantity

		    Encapsulate all the fields:
		        Conditions:
		            name can not be empty
		            unit price can not be negative
		            quantity can not be negative

		        If invalid data are given to set the firled, then make sure to throw an error duribg the runtime.
		        	(hint: you can use 'raise RuntimeError('Exception message')')


		    Add a constructor that allows user to set all the fields when the object is created.
		            (If the arguments not valid it should not be set to the instances)

		    Methods:
		        calcCost(): returns the total cost
		        toString(): returns the name, unit price, quantity and total cost info as calculated by calcCost()

"""

class Item:
    def __init__(self, name, unit_price, quantity):
        # self.__quantity = None
        # self.__unit_price = None
        # self.__name = None
        self.set_name(name)
        self.set_unit_price(unit_price)
        self.set_quantity(quantity)

    def set_name(self, name):
        if not name:
            raise RuntimeError('Name cannot be empty')
        self.__name = name

    def get_name(self):
        return self.__name

    def set_unit_price(self, unit_price):
        if unit_price < 0 :
            raise RuntimeError('Unit price cannot be negative')
        self.__unit_price = unit_price

    def get_unit_price(self):
        return self.__unit_price

    def set_quantity(self, quantity):
        if quantity < 0:
            raise RuntimeError('Quantity cannot be negative')
        self.__quantity = quantity

    def get_quantity(self):
        return self.__quantity

    def calc_cost(self):
        return self.__unit_price * self.__quantity

    def __str__(self):
        return f"Name: {self.__name}, Unit Price: {self.__unit_price}, Quantity: {self.__quantity}, Total cost: {self.calc_cost()}"


try:
    item = Item('Laptop', 1000, 3)
    print(item)
    item2 = Item('', -100, -1)
except RuntimeError as e:
    print(e)