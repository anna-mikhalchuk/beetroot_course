# Write a program that asks the answer for a mathematical expression,
# checks whether the user is right or wrong, and then responds with a message accordingly.

import random

first_number = random.randint(1, 10)
second_number = random.randint(1, 10)
operator = random.choice(["+", "-", "*", "/"])

print('Here is your task: {} {} {}'.format(first_number, operator, second_number))
answer = eval(str(first_number) + operator + str(second_number))
user_guess = input('What is the answer?')

if not user_guess.isnumeric() or float(user_guess) != float(answer):
    print('Sorry, you lose!')
else:
    print('Nice! You win')