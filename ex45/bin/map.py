import items, enemies, actions, world

class Map:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def intro_text(self):
    raise NotImplementedError()

def modify_player(self, player):
    raise NotImplementedError()

class ItemScene(Map):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)

    def adjacent_moves(self):
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):

        moves.append(actions.MoveWest())

    if world.tile_exists(self.x, self.y - 1):

        moves.append(actions.MoveNorth())

    if world.tile_exists(self.x, self.y + 1):

        moves.append(actions.MoveSouth())

    return moves

def available_actions(self):



    moves = self.adjacent_moves()

    moves.append(actions.ViewInventory())

    return moves

class EnemyScene(Map):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} lives remaining.".format(self.enemy.damage, the_player.hp))

class Beach(Map):
    def intro_text(self):
        return

    def modify_player(self, player):
        pass

class DharmaVillage(EnemyScene):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.TheOthers())

    def intro_text(self):
        if self.enemy.is_alive():
            return
        else:
            return

class PlaneWrack(ItemScene):
    def __init__(self, x, y):

        super().__init__(x, y, items.Gun())
    def intro_text(self):
        return

class Cave(EnemyScene):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.SmokeMonster())

    def intro_text(self):
        if self.enemy.is_alive():
            return
        else:
            return

class Jungle(ItemScene):
    def __init__(self, x, y):
        super().__init__(x, y, items.Stick())

    def intro_text(self):
        return

class TheOrchid(Map):
    def intro_text(self):
        return

    def modify_player(self, player):
        pass

class Camp(ItemScene):
    def __init__(self, x, y):
        super().__init__(x, y, items.ChosenOne())

    def intro_text(self):
        return

class TheHatch(Map):
    def intro_text(self):
        return

    def modify_player(self, player):
        pass
