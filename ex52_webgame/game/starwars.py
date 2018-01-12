from sys import exit
from random import randint


class Player(object):

    def __init__(self, side, health):
        self.side = side
        self.health = health
        self.weapon = []

    def append(self, weapon):
        self.weapon.append(weapon)
        return self.weapon

    def strike(self, other):
        #other.health -= randint(0,9)

class Scene(object):
    def __init__(self, title, urlname, description):
        self.title = title
        self.urlname = urlname
        self.description = description

    def enter(self, scene_player):
        exit(1)


class gameover(Scene):

    def enter(self, scene_player):
        gmo = gameover()
        print gmo
        if side == light:
            print "The dark side won and rules the galaxy now! Try again, young ...."
            return 'startscreen'
        else:
            print "The light side was stronger. This time you loose, young ...."
            return 'startscreen'

class sorry(Scene):

    def enter(self, scene_player):
        sry = sorry()
        print sry
        print "Sorry, this is not available yet. Come back later."
        return 'startscreen'


class startscreen(Scene):

    def __str__(self):
        return ""

    def enter(self, scene_player):
        sts = startscreen()
        print sts
        prin"A long time ago in a galaxy far, far away...."
        print '''
                  ________________.  ___     .______
                 /                | /   \    |   _  \
                |   (-----|  |----`/  ^  \   |  |_)  |
                 \   \    |  |    /  /_\  \  |      /
            .-----)   |   |  |   /  _____  \ |  |\  \-------.
            |________/    |__|  /__/     \__\| _| `.________|
             ____    __    ____  ___     .______    ________.
             \   \  /  \  /   / /   \    |   _  \  /        |
              \   \/    \/   / /  ^  \   |  |_)  ||   (-----`
               \            / /  /_\  \  |      /  \   \
                \    /\    / /  _____  \ |  |\  \---)   |
                 \__/  \__/ /__/     \__\|__| `._______/
        '''
        print "\n* Start Game *"
        #login?
        return 'enter'


class enter(Scene):

    def __str__(self):
        return "\nWho will you be:\n"

    def enter(self, scene_player):
        ent = enter()
        print ent
        print "Please enter your name:"
        name = raw_input("* ")
        print "Please enter your mail adress:"
        mail = raw_input("* ")
        print "Please enter a password:"
        password = raw_input("* ")
        print "Which side do you choose? Light or dark?:"
        side = raw_input("* ")
        while True:
            if side == 'light':
                side = light
            elif action == 'dark':
                side = dark
            else:
                print "You can only pick one of the above-mentioned sides:"
        print "Pick a weapon. Either a lightsaber, blaster or simply the force:"
        weapon = raw_input("* ")
        scene_player.weapon = []
        while True:
                if weapon == 'lightsaber':
                    scene_player.append(choice)
                elif weapon == 'blaster':
                    scene_player.append(choice)
                elif weapon == 'force':
                    scene_player.append(choice)
                else:
                    print "You can only pick one of the above-mentioned weapons:"

#"Enter Fight"

class episode_guide(Scene):
    def __str__(self):
        return "\nEpisode Guide\n"

    def enter(self, scene_player):
        epg = episode_guide()
        print epg
        print "Choose an episode to start from:"
        '''
        I. The Phantom Menace
            return 'phantom_menace'
        II. Attack of the Clones
            return 'clone_wars'
        III. Revenge of the Sith
            return 'sith_revenge'
        IV. A New Hope
            return 'new_hope'
        V. The Empire Strikes Back
            return 'empire_strike'
        VI. The Return of the Jedi
            return 'jedi_return'
        VII. The Force Awakens
            return 'force_awakens'
        VIII. The Last Jedi
            return 'last_jedi'
        IX. Coming Soon!
            return 'sorry'
        '''


class phantom_menace(Scene):

    def __str__(self):
        return "\nEpisode I.\n"

    def enter(self, scene_player):
        ep1 = phantom_menace()
        print ep1
        print
        '''
        Turmoil has engulfed the Galactic Republic. The taxation of trade routes to outlying star systems is in dispute.
        Hoping to resolve the matter with a blockade of deadly battleships, the greedy Trade Federation has stopped all shipping to the small planet of Naboo.
        While the congress of the Republic endlessly debates this alarming chain of events, the Supreme Chancellor has secretly dispatched two Jedi Knights,
        the guardians of peace and justice in the galaxy, to settle the conflict...."
        '''
        if side == light:
            print "You are one of these Jedi Knights, who now has to face the dark sith lord's apprentice Darth Maul."

        else:
            print "You are the dark sith lord's apprentice and have to fight these Jedi Knights."


class clone_wars(Scene):

    def __str__(self):
        return "\nEpisode II.\n"

    def enter(self, scene_player):
        ep2 = clone_wars()
        print ep2
        print
        '''
        There is unrest in the Galactic Senate. Several thousand solar systems have declared their intentions to leave the Republic.
        This separatist movement, under the leadership of the mysterious Count Dooku, has made it difficult for the limited number of Jedi Knights to maintain peace and order in the galaxy.
        Senator Amidala, the former Queen of Naboo, is returning to the Galactic Senate to vote on the critical issue of creating an ARMY OF THE REPUBLIC to assist the overwhelmed Jedi....
        '''
        if side == light:
            print "You will have to fight Count Dooku in order to stop the seperatist movement."

        else:
            print "You are the seperatist leader Count Dooku, willing to kill anyone who gets into your way."


class sith_revenge(Scene):

    def __str__(self):
        return "\nEpisode III.\n"

    def enter(self, scene_player):
        ep3 = sith_revenge()
        print ep3
        print
        '''
        War! The Republic is crumbling under attacks by the ruthless Sith Lord, Count Dooku. There are heroes on both sides.
        Evil is everywhere. In a stunning move, the fiendish droid leader, General Grievous, has swept into the Republic capital and kidnapped Chancellor Palpatine, leader of the Galactic Senate.
        As the Separatist Droid Army attempts to flee the besieged capital with their valuable hostage, two Jedi Knights lead a desperate mission to rescue the captive Chancellor....
        '''

        if side == light:
            print "Unfortunately your Padawan has joined the dark side and now turns aginst you."

        else:
            print "The dark side has won your heart, so you will do aything to help them rise to power. Even turn against your former master."


class new_hope(Scene):

    def __str__(self):
        return "\nEpisode IV.\n"

    def enter(self, scene_player):
        ep4 = new_hope()
        print ep4
        print
        '''
        It is a period of civil war. Rebel spaceships, striking from a hidden base, have won their first victory against the evil Galactic Empire.
        During the battle, Rebel spies managed to steal secret plans to the Empire's ultimate weapon, the DEATH STAR, an armored space station with enough power to destroy an entire planet. 
        Pursued by the Empire's sinister agents, Princess Leia races home aboard her starship, custodian of the stolen plans that can save her people and restore freedom to the galaxy....
        '''

        if side == light:
            print "Years later you once again meet your old student. Both of you have changed, but you still feel deeply afflicted about what has happend."

        else:
            print "Years later you once again meet your old master. Both of you have changed, but you still see the man who made you a cripple."


class empire_strike(Scene):

    def __str__(self):
        return "\nEpisode V.\n"

    def enter(self, scene_player):
        ep5 = empire_strike()
        print ep5
        print
        '''
        It is a dark time for the Rebellion. Although the Death Star has been destroyed, Imperial troops have driven the Rebel forces from their hidden base and pursued them across the galaxy.
        Evading the dreaded Imperial Starfleet, a group of freedom fighters led by Luke Skywalker has established a new secret base on the remote ice world of Hoth.
        The evil lord Darth Vader, obsessed with finding young Skywalker, has dispatched thousands of remote probes into the far reaches of space....
        '''

        if side == light:
            print "Darth Vader tells you that he is your father. You do not want to accept that and attack him."

        else:
            print "You reveal to your son Luke that you are his father. As he does not want to join you, you are forced to fight with him."


class jedi_return(Scene):

    def __str__(self):
        return "\nEpisode VI.\n"

    def enter(self, scene_player):
        ep6 = jedi_return()
        print ep6
        print
        '''
        Luke Skywalker has returned to his home planet of Tatooine in an attempt to rescue his friend Han Solo from the clutches of the vile gangster Jabba the Hutt. 
        Little does Luke know that the GALACTIC EMPIRE has secretly begun construction on a new armored space station even more powerful than the first dreaded Death Star.
        When completed, this ultimate weapon will spell certain doom for the small band of rebels struggling to restore freedom to the galaxy....
        '''

        if side == light:
            print "After getting away the last time, you meet your father once again. This time he is with the emporer himself."

        else:
            print "Your son has returned. The lesson you taught him was somehow not enough, so you will have to teach him another."

class force_awakens(Scene):

    def __str__(self):
        return "\nEpisode VII.\n"

    def enter(self, scene_player):
        ep7 = force_awakens()
        print ep7
        print
        '''
        Luke Skywalker has vanished. In his absence, the sinister FIRST ORDER has risen from the ashes of the Empire and will not rest until Skywalker, the last Jedi, has been destroyed.
        With the support of the REPUBLIC, General Leia Organa leads a brave RESISTANCE. She is desperate to find her brother Luke and gain his help in restoring peace and justice to the galaxy.
        Leia has sent her most daring pilot on a secret mission to Jakku, where an old ally has discovered a clue to Luke’s whereabouts....
        '''

        if side == light:
            print "You are an orphan child who just discovered that she has the force inside of her and can use a lightsaber. This comes in handy as you are attacked by the First Order's Kylo Ren."

        else:
            print "You are a young emotionally instable Sith with a father complex. In your world no one is going to stop you, thus you destroy everything in your way."


class last_jedi(Scene):

    def __str__(self):
        return "\nEpisode VIII.\n"

    def enter(self, scene_player):
        ep8 = last_jedi()
        print ep8
        print
        '''
        The FIRST ORDER reigns. Having decimated the peaceful Republic, Supreme Leader Snoke now deploys his merciless legions to seize military control of the galaxy.
        Only General Leia Organa’s band of RESISTANCE fighters stand against the rising tyranny, certain that Jedi Master Luke Skywalker will return and restore a spark of hope to the fight.
        But the Resistance has been exposed. As the First Order speeds toward the rebel base, the brave heroes mount a desperate escape....
        '''

        if side == light:
            print "After years of hiding you finally face your greatest fear. Your former student Kylo Ren."

        else:
            print "You sense that it is time to venge yourself against your former master Luke Skywalker."


            enemy = Player(100)

            while scene_player.health > 0 and enemy.health > 0:
                scene_player.strike(enemy)
                print "Enemy's health: %d" %enemy.health
                enemy.strike(scene_player)
                print "Your health: %d" %scene_player.health

            if scene_player.health > enemy.health:
                print "You escape the village, however severely injured."
                return 'beach'

            else:
                print "A couple of men went down, but there are way to many."
                return 'gameover'


class victory(Scene):

    def __str__(self):
        return "\nVictory!\n"

    def enter(self, scene_player):
        vic = victory()
        print vic
        print "You made it through all 8 episodes! Congratulations, you are a true fighter!"
        return 'victory'


class Map(object):

    scenes = {
        'startscreen': startscreen(),
        'enter': enter(),
        'episode_guide'
        'phantom_menace': phantom_menace(),
        'clone_wars': clone_wars(),
        'sith_revenge': sith_revenge(),
        'new_hope': new_hope(),
        'empire_strike': empire_strike(),
        'jedi_return': jedi_return(),
        'force_awakens': force_awakens(),
        'last_jedi': last_jedi(),
        'gameover': gameover(),
        'sorry': sorry(),
        'victory': victory(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

class Engine(object):

    def __init__(self, scene_map, scene_player):
        self.scene_map = scene_map
        self.scene_player = scene_player

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('victory')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter(self.scene_player)
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter(self.scene_player)

a_map = Map('startscreen')
a_player = Player(800)
a_game = Engine(a_map, a_player)
a_game.play()
