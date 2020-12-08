# Use a list comprehension to make a list containing tuples (i, j)
# where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.

first_list = []
i = 1
while i <= 10:
     first_list.append(i)
     i += 1

for j, i in enumerate(first_list):
     first_list[j] = (i, i**2)
print(first_list)