import random

class HelperMethods():
    def __init__(self):
        self.random =random
    def getRandomPetName(self):
        petNames = ["paşa", "pamuk", "duman", "tarçın", "zeytin"]
        return random.choice(petNames)

    def getRandomInt(self):
        return random.randint(1,1000)

    def getRandomTag(self):
        tags = ["tag1", "tag2", "tag3", "tag4", "tag5"]
        return random.choice(tags)

    def getRandomPetCategory(self):
        petCategories = ["Rabbits", "Mice", "Cats", "dogs"]
        return random.choice(petCategories)



