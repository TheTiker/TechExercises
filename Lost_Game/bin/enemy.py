class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0


class PolarBear(Enemy):
    def __init__(self):
        super().__init__(name="a polar bear", hp=10, damage=10)

class TheOthers(Enemy):
    def __init__(self):
        super().__init__(name="the others", hp=30, damage=20)

class SmokeMonster(Enemy):
    def __init__(self):
        super().__init__(name="the smoke monster", hp=100, damage=50)
