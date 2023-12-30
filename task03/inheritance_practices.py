"""
3. Create a python file named inheritance_practice:
		Create an abstract class named Animal:
	        Variables:
	            name, breed(final), gender(final),  age, size, color(final)

	        Encapsulate all the fields

	        Add a cosntructor that can set all the fields

	        Methods:
	            eat() ==> different animals eat different foods
	            drink() ==> all the animals drink water
	            toString() ==> to display the full info of the animal


		    Create the following subclasses of Animal:
		            Dog
		                eat(): Dog Food

		            Cat
		                eat(): Cat Food

		            Parrot
		                eat():


		            Eagle

"""
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, breed, gender, age, size, color):
        self.__name = name
        self.__breed = breed
        self.__gender = gender
        self.__age = age
        self.__size = size
        self.__color = color

    @abstractmethod
    def eat(self):
        pass

    def drink(self):
        return f"{self.__name} drinks water"

    def __str__(self):
        return f"Name: {self.__name}, Breed: {self.__breed}, Gender: {self.__gender}, Age: {self.__age}, Size: {self.__size}, Color: {self.__color}"

class Dog(Animal):
    def eat(self):
        return f"{self._Animal__name} eats Dog Food"
class Cat(Animal):
    def eat(self):
        return f"{self._Animal__name} eats Cat Food"

# Subclass Parrot
class Parrot(Animal):
    def eat(self):
        return f"{self._Animal__name} eats Seeds and Nuts"

# Subclass Eagle
class Eagle(Animal):
    def eat(self):
        return f"{self._Animal__name} eats Fish"


dog = Dog('Buddy', 'Golden Retriever', 'Male', 3, 'Medium', 'Golden')
print(dog)
print(dog.eat())
print(dog.drink())

cat = Cat('Whiskers', 'Siamese', 'Female', 2, 'Small', 'Cream')
print(cat)
print(cat.eat())
print(cat.drink())