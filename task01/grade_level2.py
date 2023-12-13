"""
14. Create a python file named grade_level2.  write a program that asks user to enter the grade level number,  determine and print which school type the person is in is in.
            grade level and types are:
                    1-5: Elementary school
                    6-8: Middle school
                    9-12: High school
                    13-16: College
                    17-18: Grad School

                    For Any Other grade: Invalid grade level given

            NOTE: MUST USE NESTED IF. DO NOT USE MORE THAN ONE PRINT STATEMENT
"""
def determine_school_type(grade_level):
    if 1 <= grade_level <= 18:
        if grade_level <= 5:
            return "Elementary School"
        if grade_level <= 8:
            return "Middle School"
        if grade_level <= 12:
            return "High School"
        if grade_level <= 16:
            return "College"
        return "Grad School"
    else:
        return "Invalid grade level given"

# Asking the user for input
grade_level = int(input("Enter your grade level number: "))
school_type = determine_school_type(grade_level)

# Displaying the result with a single print statement
print(f"You are in {school_type}")