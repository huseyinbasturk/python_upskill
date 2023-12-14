"""
17. Create a python file named crew_and_passanger, Given a number of people on the ship,
determine how many need to be crew members and how many can be passengers. Print how many of each type there should be.

            Total: 50  ====> 20 crew, 30 passengers
            Total: 75  ====> 25 crew, 50 passengers
            Total: 100 ====> 30 crew, 70 passengers
            Any other number of people on the ship is not valid

            NOTE: MUST USE NESTED IF. DO NOT USE MORE THAN ONE PRINT STATEMENT
"""
number_of_people = int(input("Enter the total number of people: "))
if number_of_people in [50, 75, 100]:
    if number_of_people == 50:
        crew, passenger = 20, 30
    elif number_of_people == 75:
        crew, passenger = 25, 50
    elif number_of_people == 100:
        crew, passenger = 30, 70
    else:
        pass
print(f"{crew} crew, {passenger} passengers")