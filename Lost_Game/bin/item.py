class Item():
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

class Fist(Weapon):
    def __init__(self):
        super().__init__(name="fist",
                         description="your own hands.",
                         value=0,
                         damage=5)

class Stick(Weapon):
    def __init__(self):
        super().__init__(name="stick",
                         description="a branch ripped off a tree.",
                         value=5,
                         damage=10)

class Gun(Weapon):
    def __init__(self):
        super().__init__(name="gun",
                         description="a handgun from the air marshal.",
                         value=10,
                         damage=20)

class ChosenOne(Weapon):
    def __init__(self):
        super().__init__(name="the chosen one",
                         description="the island's chosen one.",
                         value=100,
                         damage=50)
