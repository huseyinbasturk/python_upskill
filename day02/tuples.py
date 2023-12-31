
days = ('MON', 'TUE', 'WED', "THU", 'FRI', 'SAT', 'SUN', 1, 2, 3, 4, True, False)

print(type(days))
print(len(days))

print(days)
# days[0] = 'Java'
print(days[0])
print(days[-1])

days = ('MON', 'TUE', 'WED', "THU", 'FRI', 'SAT', 'SUN')

work_days = days[1:4]
print(work_days)

week_days = days[:-2]
print(week_days)

weekend = days[-3:]
print(weekend)

tuple1 = [1,2,3]
tuple2 = [1,2,3]
print(tuple1 == tuple2)
print(tuple1 is tuple2)

tuple3 = tuple1 + tuple2
print(tuple3)

tuple4 = tuple1 * 5
print(tuple4)

reversed_tuple1 = days[::-1]
print(reversed_tuple1)

reversed_tuple2 = tuple(reversed(days))
print(reversed_tuple2)

print(days)
print(days.index('WED'))

numbers = (10, 10, 10, 20, 30, 40)
print(numbers.count(10))

print('-------------------')

for x in days:
    print(x)

print('--------------')
for x in range(0, len(days)):
    print(x)

for x in reversed(range(0, len(days))):
    print(x)

print('-------------')

nested_tuple = ((1,2,3), (4,5,6,7,8), (9, 10))
print(len(nested_tuple))

for x in nested_tuple:
    print(x)
    for y in x:
        print(y)

for i in range(0, len(nested_tuple)):
    for j in range(0, len(nested_tuple[i])):
        print(nested_tuple[i][j])


