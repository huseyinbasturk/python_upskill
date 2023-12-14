"""
18. Create a python file named grade, a variable named grade is given. write a program to print the following messages:
            'A': excellent
            'B': great job
            'C': good
            'D': passed
            'F': failed
            other wise: invalid

            NOTE: MUST USE NESTED IF. DO NOT USE MORE THAN ONE PRINT STATEMENT

"""
grade = input("Enter your grade: ")
if grade == 'A':
    result = 'excellent'
elif grade == 'B':
    result = 'great job'
elif grade == 'C':
    result = 'good'
elif grade == 'D':
    result = 'passed'
elif grade == 'F':
    result = 'failed'
else:
    result = 'invalid'

print(result)