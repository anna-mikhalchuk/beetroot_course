# Write a program that takes your name as input, and then your age as input and greets you with the following:
# “Hello <name>, on your next birthday you’ll be <age+1> years”

name, age = input('Hi! What is your name?'), input('How old are you?')
while not name or not age.isnumeric():
    print("Sorry, I din't get it. Le's try again.")
    name, age = input('Hi! What is your name?'), input('How old are you?')
else:
    print("Hello {}, on your next birthday you'll be {} years".format(name.title(), int(age)+1))