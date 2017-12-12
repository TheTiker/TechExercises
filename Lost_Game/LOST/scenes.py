from sys import exit
from random import randint
import time

class Scene(object):

    def enter(self):
        exit(1)


class GameOver(Scene):

    def enter(self):
        print "The island got you! Game over!\n"
        exit(1)


class Beach(Scene):

    def __str__(self):
        return "\nAt the beach:\n"


    def enter(self):
        atb = Beach()
        print atb
        print "You wake up with blood and dirt all over your face."
        time.sleep(2)
        print "Lying on your back, you stare into the sun."
        time.sleep(2)
        print "The last thing you recall is sitting on a plane to Hawaii."
        time.sleep(2)
        print "You get up slowly, but your body aches and makes it difficult."
        time.sleep(2)
        print "Take a look around. Where are you?"
        time.sleep(2)
        print "A tropical beach..."
        time.sleep(2)
        print "But it is not as peaceful as it sounds."
        time.sleep(2)
        print "Smoke, fire, people screaming and dead corps all around you."
        time.sleep(2)
        print "You move through the chaos. Then you see it..."
        time.sleep(2)
        print "Your plane has crashed with its wreck now resting on the shore."
        time.sleep(2)
        print "That is when you realize:"
        time.sleep(2)
        print "\nYou are L O S T..."
        time.sleep(5)
        print "\nType enter to fight for survival, quit to commit suicide..."

        action = raw_input(">: ")

        if action == "enter":
            print "In order to survive and escape the island, you will have to make choices."
            print "These choices determine whether you will live or die."
            print "After setting up a camp with the other survivors you discover that this is not a normal island."
            print "In fact, there are strange things going on here..."
            time.sleep(10)
            return 'camp'

        elif action == "quit":
            print "You are weak and pathetic for not even trying..."
            return 'gameover'

        else:
            print "You only have two choices. Go through them again...\n"
            return 'beach'


class Camp(Scene):

    def __str__(self):
        return "\nIn the camp:\n"

    def enter(self):
        itc = Camp()
        print itc
        print "Sounds wake you up at night. Every morning you find one of you missing."
        time.sleep(3)
        print "Do you want to investigate where these noises are coming from?"
        print "Or do you want to stay in the camp?"
        print "Or search the plane wrack for weapons to defend yourself?"

        action = raw_input(">: ")

        if "investigate" in action:
            return 'jungle'

        elif "stay" in action:
            print "In the middle of the night you are dragged away by something."
            print "Then you hear a rattling sound. A flash and you are dead."
            return 'gameover'

        elif "search" in action:
            return 'planewreck'

        else:
            print "Doing nothing does not help ypu at all!"
            print "Everybody dies until you are the onyl one left."
            print "Finally the monster also takes you."
            return 'gameover'


'''
class PlaneWreck(Scene):

    def __str__(self):
        return "\nIn the plane wreck:\n"

    def enter(self):
        ipw = PlaneWreck()
        print ipw
        print "You search the plane's carcass for useful objects to defend yourself."
        print "There are several items that seem suitable, but you can only carry back three."
        print "So choose wisely!"
        time.sleep(5)
        print "There is a screw driver..."
        print "A fire extinguisher..."
        print "An inflatable vest..."
        print "A handgun..."
        print "A tazer..."
        print "A walking cane..."
        print "A photo camera..."
        print "And a lighter..."
        time.sleep(5)
        print "Pick one at a time."

        items[] = ['photo camera','handgun','lighter']
        action = raw_input(">: ")
        guesses = 0

        while items[] !== 'photo camera','handgun','lighter':

            guess = raw_input(">: ")

            if guess == items:
                print "Good choice, these might come in handy later on."
                return 'camp'

            else:
                print "Bad choice, these tools are completely useless against a monster."
                return 'camp'


'''

class Jungle(Scene):

    def __str__(self):
        return "\nIn the jungle:\n"

    def enter(self):
        itj = Jungle()
        print itj
        print "Deep inside the jungle you find the cause of these sounds."
        print "A big black cloud of smoke with lightning inside."
        print "You want to sneak away, but step on a cracking branch."
        print "The monster realizes you. You start running!"
        time.sleep(5)
        print "The path splits into three junctions, straight, left and right."
        print "Which one do you take?"

        action = raw_input(">: ")

        if action == "straight":
            print "You just want to get away from this thing."
            print "Unfortunately, the smoke monster is faster than you and catches up."
            print "It eats you up!"
            return 'gameover'

        elif action == "right":
            return 'the_hatch'

        elif action == "left":
            return 'dharmaville'

        else:
            print "Standing still is not a good option!"
            print "The monster sucks you in. You are dead!"
            return 'gameover'


class Hatch(Scene):

    def __str__(self):
        return "\nDown the hatch:\n"

    def enter(self):
        dth = Hatch()
        print dth
        print "As you are looking around to see whether the monster is still there, you trip over a hatch on the ground."
        print "It is unlocked, good for you! You climb in as fast as you can, escaping the monster's reach."
        time.sleep(2)
        print "Down there you find an entire apartment. It is built around a room with an old Apple II computer."
        print "There is a clock on the wall running down from 108 to 0 minutes."
        print "It is down to 4 minutes when an alarm goes off. You sit down at the computer."
        print "There is a note on the table with several digits on it, but the last four numbers are unreadable."
        print "You type in the 481516."
        time.sleep(5)
        print "What four digits comes next? Take a guess?"

        digits = "2342"
        guess = raw_input(">: ")

        if guess == digits:
            print "The counter resets. Everything is fine."
            print "After another 108 minutes you realize:"
            print "You are caught inside the hatch forever, as you have to enter the numbers every 108 minutes."
            return 'gameover'

        elif guess != digits:
            print "As the timer is up, some weird hieroglyphs appear on it."
            print "Then the whole island is blown up in a huge beam of bright white light!"
            return 'gameover'

        else:
            return 'gameover'


'''
class DharmaVillage(Scene):

    def __str__(self):
        return "\nWelcome to Dharam Village:\n"

    def enter(self):
        wtd = DharmaVillage()
        print wtd
        print "You see a couple of houses right in front of you and speed up to get shelter there."
        print "As you pass the gates, the monster is repelled by some invisible power."
        time.sleep(2)
        print "Before you can even realize what is going on, a group of armed people orders you to follow them."
        print "They blindfold you and bring you to there leader Ben."
        print "He offers you to teach you the island's mysteries and become a part of these others."
        time.sleep(5)
        print "You can either try to be quick and shoot all of them."
        print "Or you accept the offer."
        print "Or shout for help."

        action = raw_input(">: ")

        if "shoot" in action and items = 'gun':
            print "You pull your gun and start shooting."
            print "A couple of men go down, but there are way to many."
            print "They return the fire and injure you lethally."
            return 'gameover'

        elif "shoot" in action not and item == 'gun':
            print "You stupid idot do not even have a gun!"
            print "They get what you were up to and execute you on the village square."
            return 'gameover'

        elif "shout" in action:
            print "You are in the middle of nowhere, you fool. No one hears you."
            print "They shut your mouth, tie you to the gate and let you be eaten by the smoke monster."
            return 'gameover'

        else:
            return 'the_orchid'


'''

class Orchid(Scene):

    def __str__(self):
        return "\nIn the orchid:\n"

    def enter(self):
        ito = Orchid()
        print ito
        print "After months of living with the others, Ben brings you to their most sacred place:"
        print "The Orchid!"
        time.sleep(2)
        print "He says that this is the only place from which the island can be moved, using a magical gear."
        print "Whoever does so, however, has to make a sacrifice."
        print "For they have to leave the island and may never return."
        print "The island is in danger and thus needs to wander."
        time.sleep(5)
        print "You realize your chance and offer yourself as a sacrifice."
        print "Ben accepts your offer under one condition:"
        time.sleep(2)
        print "You have to guess behind which of the three doors the gear lies. Which do you take?"

        door = randint(1,3)
        guess = raw_input(">: ")

        if int(guess) != door:
            print "Ben rejects your offer and lets one of the others go."
            return 'the_orchid'

        else:
            print "He nods and you open door %s." % guess
            print "Everything is exactly as he described it."
            print "You trun the gear with all of your strength."
            print "Everything starts moving and a bright white light blinds you..."
            return 'escaped'


class Escape(Scene):

    def __str__(self):
        return "\nEscape:\n"

    def enter(self):
        esc = Escape()
        print esc
        print "You wake up at home, dazzled but alive."
        print "Congratulations, you escaped!"
        time.sleep(3)
        print "However, something inside of you does not feel right..."
        print "You have the urge of returning back to the island."
        time.sleep(3)
        print "But there is only one way..."
        return 'escaped'
