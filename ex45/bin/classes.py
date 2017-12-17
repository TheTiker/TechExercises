from sys import exit
import ex45

class Scene(object):

    def enter(self):
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('escaped')
        print current_scene

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()


class Map(object):

    scenes = {
        'beach': Beach(),
        'camp': Camp(),
        'planewreck': PlaneWreck(),
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
