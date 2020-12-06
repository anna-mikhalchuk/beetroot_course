# Make a list that contains all integers from 1 to 100, then find all integers from the list
# that are divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.
# Constraint: use only while loop for iteration

import random

number_list = random.sample(range(1, 100), 10)
result_list = []
print('Numbers', number_list)

i = 0
while i < len(number_list):
    if number_list[i] % 5 and not number_list[i] % 7:
        result_list.append(number_list[i])
    i += 1
if len(result_list) == 0:
    print('Sorry, nothing  to show!')
else:
    print('Result list:', result_list)