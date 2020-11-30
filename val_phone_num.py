# Make a program that checks if a string is in the right format for a phone number.
# The program should check that the string contains only numerical characters and is only 10 characters long.
# Print a suitable message depending on the outcome of the string evaluation.

attempts = 3
i = 0

while i < attempts:
    print('Hello! Please enter your phone number:')
    phone_num = input()
    i += 1
    if len(phone_num) != 10 or phone_num.isnumeric() == False:
        print('Invalid data!')
    else:
        print('Thx. Your phone number is: {}'.format(phone_num))
        i == attempts
        break
else:
    print('Sorry, you are run out of attempts')