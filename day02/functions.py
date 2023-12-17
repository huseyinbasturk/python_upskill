import numbers


def display_message():
    print("Hello World")
    print("Hello")


display_message()


def value():
    return 'Python Programming'


print(value())


def return_int() -> int:
    return 10


print(return_int())


def divide(num1, num2):
    return num1 / num2


def square(num: int):
    return num * num


print(divide(10, 2))
# print(divide('Java','Python'))

print(square(10))


# print(square(2.0))

def add(num1: numbers, num2: numbers) -> numbers:
    return num1 + num2


print(add(10, 20))
print(add(10.5, 20.5))

print('----------------------------')


def calculate(num1: numbers, num2: numbers, operator: str) -> numbers:
    if operator == '-':
        return num1 - num2
    elif operator == '+':
        return num1 + num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        print('Invalid operator')
        return 0


print(calculate(10, 20, '+'))
print(calculate(100.4, 2.5, '/'))

print('-----------------------------')


# example of method overloading

def sum(n1: numbers, n2: numbers, n3: numbers = 0, n4: numbers = 0) -> numbers:
    return n1 + n2 + n3 + n4


print(sum(10, 20))

print(sum(23, 12, 11))

print(sum(23, 12, 11, 12))


class test:
    def method(self):
        pass


print('-----------------------------')


def concat(a: str, b, c='', d='', e=''):
    print(f'{a} {b} {c} {d} {e}'.strip())


concat('Hello', 'World')
concat('Python', 'Java', 'C#', True)
concat('Python', 'Java', 'C#', 4.0, True)

"""
    1. declaring
    2. parameters
    3. restricting parameter' data type
    4. setting default value to parameter
    5. restricting return type
    
    Dynamic Typing -> any data can be assigned to variable
"""