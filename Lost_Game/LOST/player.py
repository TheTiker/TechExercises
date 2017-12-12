from random import randint
import time

class Fighter():
    def __init__(self, health):
        self.health = health

class Player(Fighter):
    def strike(self, other):
        other.health -= randint(0,9)

jedi = Player(100)
sith = Player(100)

while jedi.health > 0 and sith.health > 0:
    jedi.strike(sith)
    print "Sith's health: %d" %sith.health
    time.sleep(1)
    sith.strike(jedi)
    print "Jedi's health: %d" %jedi.health
    time.sleep(1)

if jedi.health > sith. health:
    print "the Jedi won!"
else:
    print "the Sith won!"
