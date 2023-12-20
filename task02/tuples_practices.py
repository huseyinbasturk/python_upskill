"""
10. Create a python file named tuples_practices:
        10.1 Write a program that can display the palindrome strings from a tuple of string

                Ex:
                    words = ('Java', 'Anna', 'python', 'Cydeo', 'Level')

                    output:
                        Anna
                        Level


        10.2 Write a program that can display the common elements of two lists:

                Ex:
                    tuple1 = (1,2,3,4,5)
                    tuple2 = (4,5,6,7,8)

                    Output:
                        4
                        5


        10.3 Write a program that can count the even and odd number from a tuple of integers

                Ex:
                    numbers = (1, 2, 3, 4, 5, 6, 7)

                    Output:
                        There are 3 even numbers and 4 odd numbers


"""


def display_palindromes(words):
    for word in words:
        if word.upper() == word.upper()[::-1]:
            print(word)


tuple = ('Java', 'Anna', 'python', 'Cydeo', 'Level')
print("Palindrome strings:")
display_palindromes(tuple)
print('-------------------')

def common_elements(tuple1, tuple2):
    common = set(tuple1).intersection(tuple2)
    for element in common:
        print(element)


tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
print("Common elements:")
common_elements(tuple1, tuple2)
print('-------------------')




def count_even_odd(numbers):
    even_count = sum (1 for num in numbers if num % 2 == 0)
    odd_count = sum (1 for num in numbers if num % 2 == 1)
    return even_count, odd_count


numbers = (1, 2, 3, 4, 5, 6, 7)
even_count, odd_count = count_even_odd(numbers)
print(f"There are {even_count} even numbers and {odd_count} odd numbers")

