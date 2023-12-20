"""
8. Create a python file named grade calculator, and Write a program for grade calculator:
    8.1. Ask the user "Enter your score"
            If user enters invalid score, terminate the program after displaying the error message "Invalid Entry"

    8.2 Display the grade of the student.
                    90 ~ 100 ==> A
                    80 ~ 89 ==> B
                    70 ~ 79 ==> C
                    60 ~ 69 ==> D
                    0 ~ 59 ==> F

    8.3 Ask the user would you like to continue
            If "yes" --> repeat the previous steps
            If "no" --> print "Thank you for using Cydeo Grade Calculator APP"

            If user enters an invalid entry, ask the user to re-enter until user provides a valid entry


"""

def calculate_grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score <= 89:
        return 'B'
    elif 70 <= score <= 79:
        return 'C'
    elif 60 <= score <= 69:
        return 'D'
    elif 0 <= score <= 59:
        return 'F'
    else:
        return 'Invalid Entry'

def start_up():
    while True:
        try:
            score = float(input("Enter your score: "))
            grade = calculate_grade(score)
            if grade == 'Invalid Entry':
                print(grade)
                break
            print(f"Your grade is {grade}")

            continue_choice = input("Would you like to continue (yes/no)? ").lower()
            while continue_choice not in ["yes", "no"]:
                continue_choice = input("Invalid entry. Please enter 'yes' or 'no': ").lower()

            if continue_choice == "no":
                print("Thank you for using Grade Calculator APP")
                break
        except ValueError:
            print("Invalid Entry")
            break



start_up()