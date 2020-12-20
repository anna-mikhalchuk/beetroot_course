# Write a script that creates a new output file called myfile.txt and writes the string "Hello file world!" in it.
# Then write another script that opens myfile.txt, and reads and prints its contents.
# Run your two scripts from the system command line.

with open('myfile.txt', 'w') as file:
    file.write('Hello file world!')

with open('myfile.txt') as file:
    print(file.read())