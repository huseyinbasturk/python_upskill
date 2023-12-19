"""
4. Create a python file named factorial_number, Write a program that can return the factorial number of any given number

            Ex:
                input: 5
                output: 120

                    ( because: 5! = 5 * 4 * 3 * 2* 1 = 120 )
"""


def calculate_factorial(num):
    if num == 0:
        return 1
    return num * calculate_factorial(num - 1)


number = int(input("Enter a number:\n"))
result = calculate_factorial(number)

print(f'The factorial of {number} is {result}')
