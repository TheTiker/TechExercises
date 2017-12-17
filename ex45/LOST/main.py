from scenes import *
from mapping import *
from player import *


class Engine(object):

    def __init__(self, scene_map, scene_player):
        self.scene_map = scene_map
        self.scene_player = scene_player

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('escaped')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter(self.scene_player)
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter(self.scene_player)


a_map = Map('beach')
a_player = Player(100)
a_game = Engine(a_map, a_player)
a_game.play()
