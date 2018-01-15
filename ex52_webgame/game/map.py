class Scene(object):
    def __init__(self, title, urlname, description, light_story = "", dark_story = ""):
        self.title = title
        self.urlname = urlname
        self.description = description
        self.light_story = light_story
        self.dark_story = dark_story

        self.light_actions = {}
        self.dark_actions = {}

    def action(self, useraction, lightside):
        if lightside:
          return self.light_actions.get(useraction)
        else:
          return self.dark_actions.get(useraction)

    def add_actions(self, light_actions, dark_actions):
        self.light_actions.update(light_actions)
        self.dark_actions.update(dark_actions)


intro = Scene("Intro", "intro",
'''
A long time ago in a galaxy far, far away....

          ________________.  ___     .______ 
         /                | /   \    |   _  \ 
        |   (-----|  |----'/  ^  \   |  |_)  | 
         \   \    |  |    /  /_\  \  |      / 
    .-----)   |   |  |   /  _____  \ |  |\  \-------. 
    |________/    |__|  /__/     \__\| _| `.________| 
     ____    __    ____  ___     .______    ________. 
     \   \  /  \  /   / /   \    |   _  \  /        | 
      \   \/    \/   / /  ^  \   |  |_)  ||   (-----' 
       \            / /  /_\  \  |      /  \   \ 
        \    /\    / /  _____  \ |  |\  \---)   | 
         \__/  \__/ /__/     \__\|__| `._______/  
''')


phantom_menace = Scene("I. The Phantom Menace","phantom_menace",
'''
Turmoil has engulfed the Galactic Republic. The taxation of trade routes to outlying star systems is in dispute. Hoping to resolve the matter with a blockade of deadly battleships, the greedy Trade Federation has stopped all shipping to the small planet of Naboo. While the congress of the Republic endlessly debates this alarming chain of events, the Supreme Chancellor has secretly dispatched two Jedi Knights, the guardians of peace and justice in the galaxy, to settle the conflict...."
''',
'''
You are one of these Jedi Knights, who now has to face the dark sith lord's apprentice Darth Maul. He attacks you!
Either use the FORCE, your LIGHTSABER or BLOCK the attacks.
''',
'''
You are the dark sith lord's apprentice and have to fight these Jedi Knights. You attack them!
Either use the FORCE, your LIGHTSABER or BLOCK the attacks.
''')

clone_wars = Scene("II. Attack of the Clones","clone_wars",
'''
There is unrest in the Galactic Senate. Several thousand solar systems have declared their intentions to leave the Republic. This separatist movement, under the leadership of the mysterious Count Dooku, has made it difficult for the limited number of Jedi Knights to maintain peace and order in the galaxy. Senator Amidala, the former Queen of Naboo, is returning to the Galactic Senate to vote on the critical issue of creating an ARMY OF THE REPUBLIC to assist the overwhelmed Jedi....
''',
'''
You will have to fight Count Dooku in order to stop the seperatist movement. You corner him in his headquarters!
Either use the FORCE, your LIGHTSABER or BLOCK the attacks.
''',
'''
You are the seperatist leader Count Dooku, willing to kill anyone who gets into your way. A Jedi attacks you, you fight back!
Either use the FORCE, your LIGHTSABER or BLOCK the attacks.
''')

sith_revenge = Scene("III. Revenge of the Sith","sith_revenge",
'''
War! The Republic is crumbling under attacks by the ruthless Sith Lord, Count Dooku. There are heroes on both sides. Evil is everywhere. In a stunning move, the fiendish droid leader, General Grievous, has swept into the Republic capital and kidnapped Chancellor Palpatine, leader of the Galactic Senate. As the Separatist Droid Army attempts to flee the besieged capital with their valuable hostage, two Jedi Knights lead a desperate mission to rescue the captive Chancellor....
''',
'''
Unfortunately your Padawan has joined the dark side and now turns aginst you!
Either use the FORCE, your LIGHTSABER or BLOCK the attacks.
''',
'''
The dark side has won your heart, so you will do anything to help them rise to power. Even kill your former master!
Either use the FORCE, your LIGHTSABER or BLOCK the attacks.
''')

new_hope = Scene("IV. A New Hope","new_hope",
'''
It is a period of civil war. Rebel spaceships, striking from a hidden base, have won their first victory against the evil Galactic Empire. During the battle, Rebel spies managed to steal secret plans to the Empire's ultimate weapon, the DEATH STAR, an armored space station with enough power to destroy an entire planet. Pursued by the Empire's sinister agents, Princess Leia races home aboard her starship, custodian of the stolen plans that can save her people and restore freedom to the galaxy....
''',
'''
Years later you once again meet your old pupil. Both of you have changed, but you still feel deeply afflicted about what has happend. You want to talk to him, but he attacks you!
Either use the FORCE, your LIGHTSABER or BLOCK the attacks.
''',
'''
Years later you once again meet your old master. Both of you have changed, but you still see the man who made you a cripple. You want revenge and attack him!
Either use the FORCE, your LIGHTSABER or BLOCK the attacks.
''')

empire_strike = Scene("V. The Empire Strikes Back","empire_strike",
'''
It is a dark time for the Rebellion. Although the Death Star has been destroyed, Imperial troops have driven the Rebel forces from their hidden base and pursued them across the galaxy. Evading the dreaded Imperial Starfleet, a group of freedom fighters led by Luke Skywalker has established a new secret base on the remote ice world of Hoth. The evil lord Darth Vader, obsessed with finding young Skywalker, has dispatched thousands of remote probes into the far reaches of space....
''',
'''
Darth Vader tells you that he is your father. You do not want to accept that and attack him!
Either use the FORCE, your LIGHTSABER or BLOCK the attacks.
''',
'''
You reveal to your son Luke that you are his father. As he does not want to join you, you are forced to fight with him!
Either use the FORCE, your LIGHTSABER or BLOCK the attacks.
''')

jedi_return = Scene("VI. The Return of the Jedi","jedi_return",
'''
Luke Skywalker has returned to his home planet of Tatooine in an attempt to rescue his friend Han Solo from the clutches of the vile gangster Jabba the Hutt. Little does Luke know that the GALACTIC EMPIRE has secretly begun construction on a new armored space station even more powerful than the first dreaded Death Star. When completed, this ultimate weapon will spell certain doom for the small band of rebels struggling to restore freedom to the galaxy....
''',
'''
After getting away the last time, you meet your father once again. This time he is with the emporer himself and forced to punish you!
Either use the FORCE, your LIGHTSABER or BLOCK the attacks.
''',
'''
Your son has returned. The lesson you taught him was somehow not enough, so you will have to teach him another!
Either use the FORCE, your LIGHTSABER or BLOCK the attacks.
''')

force_awakens = Scene("VII. The Force Awakens","force_awakens",
'''
Luke Skywalker has vanished. In his absence, the sinister FIRST ORDER has risen from the ashes of the Empire and will not rest until Skywalker, the last Jedi, has been destroyed. With the support of the REPUBLIC, General Leia Organa leads a brave RESISTANCE. She is desperate to find her brother Luke and gain his help in restoring peace and justice to the galaxy. Leia has sent her most daring pilot on a secret mission to Jakku, where an old ally has discovered a clue to Luke's whereabouts....
''',
'''
You are an orphan child who has just discovered that you have the force inside of you and can use a lightsaber. This comes in handy as you are attacked by First Order's Kylo Ren!
Either use the FORCE, your LIGHTSABER or BLOCK the attacks.
''',
'''
You are a young emotionally instable Sith with a father complex. In your world, no one is going to stop you, thus you destroy everything in your way, including that young woman in front of you!
Either use the FORCE, your LIGHTSABER or BLOCK the attacks.
''')

last_jedi = Scene("VIII. The Last Jedi","last_jedi",
'''
The FIRST ORDER reigns. Having decimated the peaceful Republic, Supreme Leader Snoke now deploys his merciless legions to seize military control of the galaxy. Only General Leia Organa's band of RESISTANCE fighters stand against the rising tyranny, certain that Jedi Master Luke Skywalker will return and restore a spark of hope to the fight. But the Resistance has been exposed. As the First Order speeds toward the rebel base, the brave heroes mount a desperate escape....
''',
'''
After years of hiding you finally face your greatest fear. Your former student Kylo Ren. He attacks you full of rage!
Either use the FORCE, your LIGHTSABER or BLOCK the attacks.
''',
'''
You sense that it is time to venge yourself against your former master Luke Skywalker. Only his death will fulfill you!
Either use the FORCE, your LIGHTSABER or BLOCK the attacks.
'''
)

victory = Scene("Victory!", "victory", "")

game_over = Scene("Game over!", "game_over", "")


phantom_menace.add_actions(
{
  'block': 2,
  'lightsaber': 1,
  'force': -1
},
{
  'block': 2,
  'lightsaber': 1,
  'force': -1
})

clone_wars.add_actions(
{
  'block': 2,
  'lightsaber': 1,
  'force': -1
},
{
  'block': 2,
  'lightsaber': 1,
  'force': -1
})

sith_revenge.add_actions(
{
  'block': 2,
  'lightsaber': 1,
  'force': -1
},
{
  'block': 2,
  'lightsaber': 1,
  'force': -1
})

new_hope.add_actions(
{
  'block': 2,
  'lightsaber': 1,
  'force': -1
},
{
  'block': 2,
  'lightsaber': 1,
  'force': -1
})

empire_strike.add_actions(
{
  'block': 2,
  'lightsaber': 1,
  'force': -1
},
{
  'block': 2,
  'lightsaber': 1,
  'force': -1
})

jedi_return.add_actions(
{
  'block': 2,
  'lightsaber': 1,
  'force': -1
},
{
  'block': 2,
  'lightsaber': 1,
  'force': -1
})

force_awakens.add_actions(
{
  'block': 2,
  'lightsaber': 1,
  'force': -1
},
{
  'block': 2,
  'lightsaber': 1,
  'force': -1
})

last_jedi.add_actions(
{
  'block': 2,
  'lightsaber': 1,
  'force': -1
},
{
  'block': 2,
  'lightsaber': 1,
  'force': -1
})


EPISODES = [
    phantom_menace,
    clone_wars,
    sith_revenge,
    new_hope,
    empire_strike,
    jedi_return,
    force_awakens,
    last_jedi,
]

SCENES = {
    intro.urlname : intro,
    phantom_menace.urlname : phantom_menace,
    clone_wars.urlname : clone_wars,
    sith_revenge.urlname : sith_revenge,
    new_hope.urlname : new_hope,
    empire_strike.urlname : empire_strike,
    jedi_return.urlname : jedi_return,
    force_awakens.urlname : force_awakens,
    last_jedi.urlname : last_jedi,
    victory.urlname : victory
}

START = phantom_menace
INTRO = intro
