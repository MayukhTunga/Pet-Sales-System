from pet import *

class Bird(Pet):
    def getAttributes(self, name, gender, dob, age, height, weight, breed, talk, fly):
        self.name = name
        self.gender = gender
        self.dob = dob
        self.age = age
        self.height = height
        self.weight = weight
        self.breed = breed
        self.talk = talk
        self.fly = fly
