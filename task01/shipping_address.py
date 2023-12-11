"""
3. Create a python file named ShippingAddress. Declare the following variables:
                    name
                    building_number
                    street_name
                    city
                    state
                    zip_code

    Use concatenation to print the full shipping address

        Ex:
            Given data:
                name = "Aaron Kissinger"
                building_number = 13621A
                street_name = "Legacy Circle"
                city = "Fairfax"
                state = "VA"
                zip_code = 22030

            Output:
                Your shipping addrees is:
                        Aaron Kissinger
                        13621A Legacy Circle
                        Fairfax, VA 22030
"""

name = "Aaron Kissinger"
building_number = 13621
street_name = "Legacy Circle"
city = "Fairfax"
state = "VA"
zip_code = 22030

print(f"Your shipping address is:\n\t{name}\n\t{building_number} {street_name}\n\t{city}, {state} {zip_code}")