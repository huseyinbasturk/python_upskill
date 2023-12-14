"""
20. Create a python file named browser. Write a program that can display the name of selected browser
        1. declare a String variable named browser_name
        2. Assume that the valid browsers are: chrome, firefox, opera, safari, edge.
        3. if the browser name does not match with the valid browser names, out put should be: Invalid Browser Name

        Ex:
            String browser = "chrome";

        Output:
            Chrome Browser is selected

        Note: MUST use nested if
"""
browser_name = input("Enter browser name: ")
valid_browsers = ["chrome", "firefox", "opera", "safari", "edge"]
if browser_name.lower() in valid_browsers:
    print(f"{browser_name.capitalize()} Browser is selected")
else:
    print("Invalid Browser Name")