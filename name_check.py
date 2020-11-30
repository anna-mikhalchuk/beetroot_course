# Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input.
# The program should check if your input is equal to the stored name even if the given name has another case,
# e.g., if your input is “Anton” and the stored name is “anton”, it should return True.

name = 'anna'
print('Hello! Please enter your name:')
new_name = input()

if name == new_name.lower():
    print(name == new_name.lower())
    print('Hello {}. Nice to meet you!'.format(new_name))
else:
    print('Sorry, there is a mistmatch')