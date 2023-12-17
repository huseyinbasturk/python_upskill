name = 'Python'

print(len(name))
print(name[0])
print(name[len(name)-1])

print(name[-1])
print(name[-2])

s = 'Java Programming Language'
s2 = s[5:16]

print(s2)

s3 = s[:4]
print(s3)

s4 = s[::-1]  # reverses the string after slicing
print(s4)

s = 'Python Programming'
s5 = str(reversed(s))
print(type(s5))
reversed(s5)
print(s5)
s5 = s[::-1]

s5 = 'python programming'

s6 = s5[7:]
print(s6)


print('----------------------------')
s = 'python programming'
print(s.capitalize())  # Python programming
print(s.title())    # Python Programming

s = "      Python   "
s = s.strip()
print(s)

s = 'Java Java'
print(s.index('a'))
print(s.rindex('a'))

s = s.replace('Java', 'Python',1)
print(s)

s = 'C# C# Python'
s = s.replace(' C# ', ' Java ')
print(s)

s = 'Java Java Java Python Python'
count_java = s.count('Java')
count_python = s.count('Python')
print(count_java)
print(count_python)

s1 = 'java'
s2 = 'JAVA'

print(s1.lower() == s2.lower())

s = 'Java'
print(s[0].islower())
print(s[0].isupper())

s = 'a'
print(s.isalpha())

s='1'
print(s.isdigit())

