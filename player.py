from random import randint

class Player(object):
    
    def __init__(self, health):
        self.health = health
        self.items = []

    def append(self, item):
        self.items.append(item)
        return self.items

    def strike(self, other):
        other.health -= randint(0,9)
