"""
1. Create a python file named list_practices:

		1.1 Write a program that can move all the zeros to the last indexes of ArrayList
	            Ex:
	                list: [1,0,2,0,3,0,4,0]

	            output:
	                [1, 2, 3, 4, 0, 0, 0, 0]


	    1.2 write a program that can multiply each odd number by 2
		            ex:
		            	list = [1,2,3,4,5];

		                output: [2,2,6,4,10]


	    1.3 Write a program that can remove all the names "Ahmed" from a list of strings
				Ex:
	                list = ["John", "Ahmed", "Daniel", "Ahmed", "James", "Muhammed"]

	            output:
	            	["John", "Daniel", "James", "Muhammed"]


		1.4 Write a program that can display the palindrome strings from a list of String
				Ex:
					words = ['Java', 'Anna', 'python', 'Cydeo', 'Level']

					output:
						Anna
						Level


		1.5 Write a program that can display the common elements of two lists:
				Ex:
					list1 = [1,2,3,4,5]
					list2 = [4,5,6,7,8]

					Output:
						4
						5

		1.6 Write a program that can remove the duplicated elements from a list
				Ex:
					elements = [1,2,3,4,5,1,2,3,4,5]

					Output:
						[1, 2, 3, 4, 5]

					Notes: Do Not use Set


		1.7 Write a program that can remove string elements from a list if the firt and last characters of the string are same
				ex:
					list = {"Anna", "Canada", "Bob", "David", "Lan", "Abida", "Ebrahim", "Farida"}

				output:
					["Lan", "Ebrahim", "Farida"]


		1.8  Write a program that can display the unique elements of an arrayList:
					ex:
						list = [1, 1, 2, 3, 3, 4, 5, 5]

					output:
						[2, 4]

"""

def move_zeros(list):
    non_zeros = [num for num in list if num !=0]
    zeros = [0] * list.count(0)
    return non_zeros + zeros

list = [1,0,2,0,3,0,4,0]
print(move_zeros(list))

print('------------------------')
def multiply_odds(list):
    return [num * 2 if num % 2 != 0 else num for num in list]

list = [1,2,3,4,5]
print(multiply_odds(list))


print('------------------------')

def remove_ahmed(list):
    return [name for name in list if name.upper() != 'AHMED' ]


list = ["John", "Ahmed", "Daniel", "Ahmed", "James", "Muhammed"]
print(remove_ahmed(list))

print('------------------------')

def display_palindromes(words):
    return [word for word in words if word.lower() == word.lower()[::-1]]

words = ['Java', 'Anna', 'python', 'Cydeo', 'Level']
print(display_palindromes(words))

print('------------------------')
def common_elements(list1, list2):
    return [set(list1).intersection(set(list2))]


list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]
print(common_elements(list1, list2))

print('------------------------')

def remove_duplicates(list):
    return [list[i] for i in range(len(list)) if list[i] not in list[:i]]


elements = [1,2,3,4,5,1,2,3,4,5]
print(remove_duplicates(elements))

print('------------------------')

def remove_same_first_last(list):
    return [word for word in list if word.lower()[0] != word.lower()[-1]]

list = {"Anna", "Canada", "Bob", "David", "Lan", "Abida", "Ebrahim", "Farida"}
print(remove_same_first_last(list))

print('------------------------')

def unique_elements(list):
    return [num for num in list if list.count(num) == 1]

list = [1, 1, 2, 3, 3, 4, 5, 5]
print(unique_elements(list))



