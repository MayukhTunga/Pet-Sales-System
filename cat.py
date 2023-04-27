from pet import *

class Cat(Pet):
    def isFriendly(self, friendly):
        self.friendly = friendly

    def respondsToName(self, responds):
        self.responds = responds