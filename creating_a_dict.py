# Create a function called make_country, which takes in a country’s name and capital as parameters.
# Then create a dictionary from those parameters, with ‘name’ and ‘capital’ as keys.
# Make the function print out the values of the dictionary to make sure that it works as intended.

def make_country(**kwargs):
    print('Country', '-', 'Capital')
    for name, capital in kwargs.items():
        print(name, '-', capital)
    return

make_country(UA = "Kyiv", CA = 'Ottawa', Germany = 'Berlin')