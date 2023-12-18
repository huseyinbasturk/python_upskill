"""
2. Create a python file named numbers, Write a program that asks user to enter
number for 5 times, and print how many positive and negative numbers user entered
            Ex:
                Inputs:
                    10
                    20
                    -1
                    0
                    3

                Output:
                    3 positive and 1 negative


"""


def count_positives_negatives(numbers):
    positive_count = sum(1 for num in numbers if num > 0)
    negative_count = sum(1 for num in numbers if num < 0)
    return positive_count, negative_count


entered_numbers = [int(input("Enter a number: ")) for x in range(5)]

positive_count, negative_count = count_positives_negatives(entered_numbers)

print(f"{positive_count} positive and {negative_count} negative")


