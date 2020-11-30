# Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
# If the string length is less than 2, return instead of the empty string.

# Sample String: 'helloworld'
# Expected Result : 'held'

# Sample String: 'my'
# Expected Result : 'mymy'

# Sample String: ' x'
# Expected Result: Empty String

string_world = 'helloworld'
string_my = 'my'
string_x = ' x'

if len(string_world) < 2 or string_world.isalpha() == False:
     print('Less than 2 alphabetic chars')
else:
     print('World string: {}'.format(string_world[0:2] + string_world[-2:]))

# print('Empty string:'.format(string_x.strip('x')))
if len(string_my) < 2 or string_my.isalpha() == False:
     print('Less than 2 alphabetic chars')
else:
     print('My string: {}'.format(string_my[0:2] + string_my[-2:]))

if len(string_x) < 2 or string_x.isalpha() == False:
     print('Less than 2 alphabetic chars')
else:
     print('X string: {}'.format(string_x[0:2] + string_x[-2:]))