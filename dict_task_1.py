# Make a program that has some sentence (a string) on input and
# returns a dict containing all unique words as keys and the number of occurrences as values.

my_string = input('Please, enter your sentence').split()
print('Split', my_string)

new_list = []
for key in my_string:
    new_list.append(my_string.count(key))
#print('New List:', new_list)

my_dict = {my_string[i] : new_list[i] for i in range(0, len(my_string))}
print('Dict:', my_dict, type(my_dict))