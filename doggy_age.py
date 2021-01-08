# Create a class Dog with class attribute `age_factor` equals to 7.
# Make __init__() which takes values for a dog’s age.
# Then create a method `human_age` which returns the dog’s age in human equivalent.

class Dog:
    age_factor = 7

    def __init__(self, dogAge):
        self.dogAge = dogAge
        self.humanAge = 1

    def human_age(self):
        self.humanAge = Dog.age_factor * self.dogAge
        print(f'The dog’s age in human equivalent is {self.humanAge}')

doggy = Dog(3)
doggy.human_age()
doggydog = Dog(6)
doggydog.human_age()