"""
6. Create a python file named sum_of_digits, Write a program that can return the sum of digits from a  string
             Ex:
                 input: A1B2C3

                 output: 6
"""

def sum_of_digits(s):
    return sum(int(char) for char in s if char.isdigit())


input_string = input("Enter a string:\n")
result = sum_of_digits(input_string)

print(f"The sum of digits in the string is {result}")
