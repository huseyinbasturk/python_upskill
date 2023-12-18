"""
1.Create a python file named functions_practices:
    1.1 Create a function that can check if a person is eligible to vote
                Ex:
                    eligibleToVote(19, "USA");

                output:
                    You are not eligible to vote!

    1.2 Create a function that can calculate the grade of the student based on the score

    1.3 Create a function that can if the given integer is positive, negative or zero

    1.4 Create a function that can check if a string is palindrome, the function
    should return true if the given string is palindrome.
"""
import numbers


def eligible_to_Vote(age: numbers, country: str):
    if age >= 18 and country.upper() == 'USA':
        return "You are eligible to vote!"
    else:
        return "You are not eligible to vote!"


def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


def check_number(num):
    if num > 0:
        return 'Positive'
    elif num < 0:
        return 'Negative'
    else:
        return 'Zero'


def is_palindrome(str):
    return str.upper() == str[::-1].upper()


print(eligible_to_Vote(18, "usa"))
print(calculate_grade(88))
print(check_number(-4))
print(is_palindrome('Radar'))

