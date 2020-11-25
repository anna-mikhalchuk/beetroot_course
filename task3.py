# Write a program, which has two print statements to print the following text:
# (capital letters “O” and “H”, made from “#” symbols)
# Pay attention that usage of spaces is forbidden, as well as
# creating the whole result text string using “”” ”””, use ‘\n’ and ‘\t’ symbols instead.

print("##########", end = '\n')
print("#", end = '\t\t # \n')
print("#", end = '\t\t # \n')
print("#", end = '\t\t # \n')
print("##########", end = '\n\n')

print("#", end = '\t\t # \n')
print("#", end = '\t\t # \n')
print("##########", end = '\n')
print("#", end = '\t\t # \n')
print("#", end = '\t\t # \n\n')

# Definitely this one could be simplified as well (print(symbol, end = '\t # \n'))
symbol = '#'
print(symbol, end = '\t # \n')
print(symbol, end = '\t # \n')
print(symbol*6, end = '\n')
print(symbol, end = '\t # \n')
print(symbol, end = '\t # \n\n')

# Definitely this one could be simplified as well
print(symbol, symbol, sep = '\t\t', end = '\n')
print(symbol, symbol, sep = '\t\t', end = '\n')
print(symbol*9, end = '\n')
print(symbol, symbol, sep = '\t\t', end = '\n')
print(symbol, symbol, sep = '\t\t', end = '\n')