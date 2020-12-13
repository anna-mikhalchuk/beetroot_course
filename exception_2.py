# Write a function that takes in two numbers from the user via input(), call the numbers a and b,
# and then returns the value of squared a divided by b, construct a try-except block which raises an exception
# if the two values given by the input function were not numbers, and if value b was zero (cannot divide by zero).

def my_function(*args):
    try:
        a = float(input('Enter a first number: '))
        b = float(input('Enter a second number: '))
        result = (a * a) / b
        print(f'Here is your {result}')
    except ValueError:
        print('Not a number!')
    except ZeroDivisionError:
        print('Cannot divide by zero!')

my_function()