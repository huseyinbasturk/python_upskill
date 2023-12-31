try:
    num = 10 / 0
    print(num)
except:
    print('Something went wrong')
else:
    print('Nothing went wrong')
finally:
    print('finally block')

print('Test completed')

print('-------------')

tuple1 = (10,20,30,40)
try:
    print(tuple1[2])
except:
    print('The index number is too large')
else:
    print('The index number is valid')

print('--------------')
try:
    raise FileNotFoundError('No such a file')
except SyntaxError:
    print('Syntax error')
except OSError:
    print('OS Error')
except ArithmeticError:
    print('arithmetic error')
# else:
#     print('No error')
finally:
    print('finally block')

print('----------------')

