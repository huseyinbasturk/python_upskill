"""
21. Create a python file named number_to_words, Write a program that can convert user entered number (from 0~9) to words.

    NOTE: MUST use ternary
"""


def number_to_word(number):
    return {
        0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four",
        5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
    }.get(number, "Invalid number")


# Asking the user for input
number = int(input("Enter a number (0-9): "))
word = number_to_word(number)

print(word)
