import json

path = 'files/Test.json'

json_file = open(path, 'r')

dictionary = json.load(json_file)
print(dictionary)

for x in dict(dictionary).keys():
    print(x)

json_file.close()

print('------------------ writing json file ----------------')

dictionary['name'] = 'Aaron King'
dictionary['age'] = 45

print(dictionary)

students = {
    'A01': {
        'name': 'James',
        'gender': 'Male',
        'gpa': 3.5,
        'subjects': ['Math', 'Physics']
    },
    'A02': {
        'name': 'Hazel',
        'gender': 'Female',
        'gpa': 3.0,
        'subjects': ['Biology', 'Programming']
    },
    'A03': {
        'name': 'Yulia',
        'gender': 'Female',
        'gpa': 4,
        'subjects': ['Chemistry', 'Programming']
    }
}

#
# json_file = open('files/Test2.json', 'w')
#
# json_object = json.dumps(dictionary, indent=2)
#
# json_file.write(json_object)

json_file = open('files/Test2.json', 'w')
json_object = json.dumps(students, indent=2) # converting dictionary to json object
json_file.write(json_object)
json_file.close()