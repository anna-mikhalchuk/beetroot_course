# Make a program that has your name and the current day of the week stored as separate variables
# and then prints a greeting message

from datetime import datetime # https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior

# f-strings
today = datetime.today().strftime('%A')
first_name = 'anna'
print(f"Good day {first_name.capitalize()}! {today} is a perfect day to learn some python.")

# concatenation, placeholders (direct order)
print('--------')
lang = 'python'
greeting = 'Good day {}, {} is a perfect day to learn some '
greeting += lang
print(greeting.format(first_name.capitalize(), today, lang), end = '.\n')

# placeholders (indexing)
print('--------')
print('Good day {1}, {0} is a perfect day to learn some python.'.format(today, first_name.capitalize()))

# %s
print('--------')
print('Good day %s, %s is a perfect day to learn some python.' % (first_name.capitalize(), first_name))

# Save your first and last name as separate variables,
# then use string concatenation to add them together with a white space in between and print a greeting.
print('--------')
last_name = 'mikhalchuk'
name = first_name + ' ' + last_name
print(greeting.format(name.title(), today), end = '!')