import logging

logging.basicConfig(level="INFO")

class UnformattedAnimal:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

class FormattedAnimal:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.breed}"

mochi_cat = UnformattedAnimal("Mochi", 4, "Cat")
logging.info("UnformattedAnimal: %s", mochi_cat)

sally_dog = FormattedAnimal("Sally", 14, "Dog")
logging.info("FormattedAnimal: %s", sally_dog)
