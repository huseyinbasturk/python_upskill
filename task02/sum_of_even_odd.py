"""
3. Create a python file named sum_of_even_odd:
        3.1 Write a program that can return the sum of even numbers between 1 to 100

        3.2 Write a program that can return the sum of odd numbers between 1 to 100

        3.3 write a program that can calculate the sum of all numbers between 1 to any given number
            ex:
                input: 100
                output: 5050

                input: 50
                output: 1275
"""
sum_even = sum(number for number in range(1,100) if number % 2 == 0)

sum_odd = sum(number for number in range(1,100) if number % 2 != 0)

def sum_of_numbers(n):
    return sum(range(1, n+1))

print(f"Sum of even numbers between 1 to 100: {sum_even}")
print(f"Sum of odd numbers between 1 to 100: {sum_odd}")

number = int(input("Enter a number:\n"))
print(f"Sum of numbers up to {number}: {sum_of_numbers(number)}")



