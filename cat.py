from pet import *

class Cat(Pet):
    def getAttributes(self, name, gender, dob, age, height, weight, breed, friendly, responds):
        self.name = name
        self.gender = gender
        self.dob = dob
        self.age = age
        self.height = height
        self.weight = weight
        self.breed = breed
        self.friendly = friendly
        self.responds = responds
    