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