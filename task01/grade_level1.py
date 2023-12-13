"""
13.  Create a python file named grade_level1.  write a program that asks user to enter the grade level number,  determine and print which school type the person is in is in.
            grade level and types are:
                    1-5: Elementary school
                    6-8: Middle school
                    9-12: High school
                    13-16: College
                    17-18: Grad School

              Assume that the given number is 1 ~ 18
"""

grade_level = int(input("Enter grade level: "))
if 1 < grade_level <6:
    print("Elementary School")
elif 6 <= grade_level < 9:
    print("Middle School")
elif 9 <= grade_level < 13:
    print("High School")
elif 13 <= grade_level < 17:
    print("College")
elif 17 <= grade_level < 19:
    print("College")
else:
    print('Invalid grade')