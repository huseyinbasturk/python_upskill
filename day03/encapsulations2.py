
class Person:

    def __init__(self, name: str = 'Jimmy', age: int = 2):
        self.__name = None
        self.__age = None
        self.person_name = name
        self.person_age = age

    @property
    def person_name(self):
        if self.__name is None or self.__name == '' or type(self.__name) != str:
            raise RuntimeError(f'Invalid name has been set: {self.__name}')
        return self.__name

    @person_name.setter
    def person_name(self, value):
        if type(value) != str:
            raise RuntimeError(f'Person name must be string')

        if value == '':
            raise RuntimeError(f'Person name cannot be empty')
        self.__name = value


    @property
    def person_age(self):
        return self.__age

    @person_age.setter
    def person_age(self, value):
        if value < 0 or value >150:
            raise RuntimeError(f'Invalid age {value}')

        self.__age = value

    def __str__(self):
        return str(self.__dict__)


person1 = Person()

person1.person_name = 'Daniel'
print(person1.person_name)