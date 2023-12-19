"""
5. Create a python file named characters, write a program that can retrive the digits, letters and special characters from a string
            Ex:
                input:
                    mn@#123Ab!

                output:
                    letters: mnAb
                    digits: 123
                    special chars: @#!

"""


def separate_characters(s):
    digits = ''.join(char for char in s if char.isdigit())
    letters = ''.join(char for char in s if char.isalpha())
    special_chars = ''.join(char for char in s if not char.isdigit() and not char.isalpha())
    return digits, letters, special_chars


input_string = input("Enter a string:\n")
digits, letters, special_chars = separate_characters(input_string)


print(f'letters: {letters}')
print(f'digits: {digits}')
print(f'special chars: {special_chars}')
