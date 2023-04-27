from pet import *

class Bird(Pet):
    def canTalk(self, talk):
        self.talk = talk

    def canFly(self, fly):
        self.fly = fly