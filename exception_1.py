# Write a function called oops that explicitly raises an IndexError exception when called.
# Then write another function that calls oops inside a try/except statement to catch the error.
# What happens if you change oops to raise KeyError instead of IndexError?

def oops():
    raise IndexError

def my_function():
    try:
        oops()
    except IndexError:
        print('Oops Index error!')

my_function()

# def oops(key, index, **kwargs):
#     try:
#         print(fruits_dict[key][index])
#     except IndexError:
#         print('Oops Index error!')
#     except KeyError:
#         print('Oops Key Error!')
#
# fruits_dict = {'a': ['Apples', 'Apricots', 'Avocados'],
#                    'b': 'Bananas',
#                    'c': ['Cherries', 'Cucumbers']}
#
# oops('d', 1,  fruits_dict = fruits_dict)