# Make a program with 2 numbers saved in separate variables a and b, then print the results:

a, b = 2, 5.3
print('a: {0}, b: {1}'.format(type(a), type(b)))

# Addition
print('Addition:', a+b)

# Subtraction
subtraction = a-b
print('Subtraction:', subtraction)

# Division
division = 'Division: {} by itself ='
print(division.format(a), a/a)

# Multiplication
multiplication = f'Multiplication: {a} * {b} ='
print(multiplication, a*b)

# Exponent (Power)
exponent = a**b
print(round(exponent, int(b)), end = ' Exponent Result! \n')

# Modulus
modulus = b%a
print('Modulus b%a =', modulus)

# Floor division
print('--------')
b //= a
number_list = f'a: {a}, b: {b}'
print("""With provided requirements: {}. 
The result of floor division is: {}""".format(number_list, b))
print('--------')