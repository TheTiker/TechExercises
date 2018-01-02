from scenes import *

class Map(object):

    scenes = {
        'beach': Beach(),
        'camp': Camp(),
        'plane_wreck': PlaneWreck(),
        'jungle': Jungle(),
        'the_hatch': Hatch(),
        'dharmaville': DharmaVillage(),
        'the_orchid': Orchid(),
        'gameover': GameOver(),
        'escaped': Escape(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)
