
# unique_elements = {}  ->make it dict
unique_elements = set()
unique_elements.add(10)
unique_elements.add(10)
unique_elements.add(10)
unique_elements.add(20)
unique_elements.add(20)

print(type(unique_elements))
print(unique_elements)

unique_elements.remove(10)
print(unique_elements)

unique_elements.update({1,2,3,4})
print(unique_elements)

# print(help(set.update))
# print(help(str.istitle))

n = unique_elements.pop()
print(n)
print(unique_elements)

print('-----------------')

print('----------- difference -------------')
# compares two sets and returns a new set which contains the items that only exist in first set
s1 = {'Java', 'Python', 'C#'}
s2 = {'Ruby', 'Java', 'C++', 'Swift'}

s3 = s1.difference(s2)
print(s3)


print('----------- intersection -------------')
# compares two sets and returns a new set which contains common elements of two sets
s1 = {'Java', 'Python', 'C#'}
s2 = {'Ruby', 'Java', 'C++', 'Swift', 'Java', 'Python'}

s3 = s1.intersection(s2)
print(s3)

print('----------- difference update -------------')
# removes the elements of the first set that exist in the second set
a1 = {'Book', 'Pen', 'Apple', 'Cherry', 'Coffee'}
a2 = {'Book', 'Apple', 'Banana', 'Grape', 'TV'}

a1.difference_update(a2)
print(a1)


print('----------- intersection update -------------')
# removes the uncommon elements of the first & second set
b1 = {'Book', 'Pen', 'Apple', 'Cherry', 'Coffee'}
b2 = {'Book', 'Apple', 'Banana', 'Grape', 'TV'}

b1.intersection_update(b2)
print(b1)

print('----------- symmetric difference -------------')
# compares two sets and returns a new set which contains all elements except the common once
e1 = {'Apple', 'Cherry', 'Banana'}
e2 = {'Strawberry', 'Apple', 'Banana', 'Grape', 'Mango', 'Lemon'}

e3 = e1.symmetric_difference(e2)
print(e3)

