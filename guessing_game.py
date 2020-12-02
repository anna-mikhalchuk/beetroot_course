# Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
# The result should be sent back to the user via a print statement.

import random

number = random.randint(1, 10)
print("Hey. Let's play a game!")
user_guess = input('Guess a number (1-10):')

if not user_guess.isnumeric() or int(user_guess) not in range(1, 10):
    print("Sorry. Incorrect input!")
else:
    while int(user_guess) != number:
        print("I'll give you another chance")
        user_guess = input('Guess a number (1-10):')
        if not user_guess.isnumeric() or int(user_guess) not in range(1, 10):
            print("Sorry. Incorrect input!")
            break
    else:
        print('Nice catch! My number was: {}'.format(number))