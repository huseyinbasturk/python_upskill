#import utility
from utility import sum, calculate  # similar to static import

result = sum(10,20)
print(result)

result = calculate(10,200, '+')

print(result)

# import utility
# utility.concat()
# utility.sum()
# utility.calculate()

print('-------------------------')

import utility as u
u.concat('H', 'B')

print('-------------------------')

from utility import sum as s
result = s(1,2,3)
print(result)