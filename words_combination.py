# Create a program that reads an input string and then creates and prints 5 random strings from characters of the input string.

# For example, the program obtained the word ‘hello’,
# so it should print 5 random strings(words) that combine characters ‘h’, ‘e’, ‘l’, ‘l’, ‘o’ -> ‘hlelo’, ‘olelh’, ‘loleh’
# Tips: Use random module to get random char from string)

import random

i = 0
chars = input('Please, enter your string ')
if not chars:
    print('Nothing to show')
else:
    while i < len(chars): #if not some_string:
        new_string = ''.join(random.choice(chars) for _ in range(len(chars)))
        print(i+1, 'New string', new_string)
        i += 1