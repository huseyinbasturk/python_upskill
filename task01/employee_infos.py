"""
11. Create a python file named employee_info:
            Ask the user to enter the following info, and diplsay the user entered info:
                        name (String)
                        age (integer)
                        gender (String)
                        company (String)
                        job title (String)
                        salary (float)

            Ex:
                Given Data:
                    name = "Daniel"
                    age = 28
                    gender = 'Male'
                    company_name = 'Google Inc'
                    job_title = "Scrum Master"
                    salary = 90000


                Output:
                    Daniel is 28 years old, gender is Male
                    Daniel works at Google Inc as a Scrum Master
                    Daniel makes $ 90000 per year

"""

name = input("Enter your name\n")
age = input("Enter your age\n")
gender = input("Enter your gender\n")
company_name = input("Enter company name\n")
job_title = input("Enter your job title\n")
salary = input("Enter your salary\n")

print(f"{name} is {age} years old, gender is {gender}\n{name} works at {company_name} as a {job_title}\n{name} makes $ {salary} per year")