# Write a Python program to get the largest number from a list of random numbers
# with the length of 10
# Constraints: use only while loop and random module to generate numbers

import random

# while loop
num_list = []
i = 0
while i < 10:
    num_list.append(random.randint(1,50))
    i += 1
print('Numbers', num_list)

i = 0
greatest = num_list[i]
while i < len(num_list):
    if num_list[i] > greatest:
        greatest = num_list[i]
    i += 1
print('The greatest number in list:', greatest)

# easy way
# number_list = random.sample(range(1, 50), 10)
# print('Numbers', number_list)
# i = 0
# greatest = number_list[i]
# while i < len(number_list):
#     if number_list[i] >= greatest:
#         greatest = number_list[i]
#     i += 1
# print('The greatest number in list:', greatest)

# the easiest way
# number_list.sort(reverse=False)
# x = len(number_list)
# print('The greatest number in list:', number_list[x-1])

