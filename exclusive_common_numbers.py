# Generate 2 lists with the length of 10 with random integers from 1 to 10,
# and make a third list containing the common integers between the 2 initial lists without any duplicates.
# Constraints: use only while loop and random module to generate numbers
import random

first_list = []
second_list = []
final_list = []

i = 0
while i < 10:
    first_list.append(random.randint(1, 10))
    second_list.append(random.randint(1, 10))
    i += 1
print(f'First {first_list} \nSecond {second_list}')

i = 0
while i < 10:
    if first_list[i] in second_list and not first_list[i] in final_list:
        final_list.append(first_list[i])
    i += 1

validation = set(first_list) & set(second_list)
print(f'Validation list: {sorted(validation)} \nFinal list: {sorted(final_list)}')