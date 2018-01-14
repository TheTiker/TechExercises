from flask import Flask, session, request
from flask import url_for, redirect, render_template
from random import randint
import map


app = Flask(__name__)
    
def strike(bonus):
    player_health = session['player_health']
    enemy_health = session['enemy_health']

    if bonus > 0:
      player_health += bonus
    elif bonus < 0:
      enemy_health -= bonus
    else:
      player_health -= randint(0,9)
      enemy_health -= randint(0,9)

    if player_health < 0:
      player_health = 0;

    if enemy_health < 0:
      enemy_health = 0; 

    session['player_health'] = player_health
    session['enemy_health'] = enemy_health

    if player_health == 0:
      return -1
    elif enemy_health == 0:
      return 1
    return 0; 


def reset_health():
    player_health = session['player_health']
    enemy_health = session['enemy_health']

    if player_health < 100:
      player_health = 100;
      session['player_health'] = player_health

    if enemy_health < 100:
      enemy_health = 100;
      session['enemy_health'] = enemy_health


@app.route('/intro', methods=['GET'])
def intro_get():    
    session['player_health'] = 100;
    session['enemy_health'] = 100;
    user_name = session['username']
    if user_name is None:
      user_name = ""
    thescene = map.SCENES[session['scene']]
    return render_template('intro.html', scene=thescene, username=user_name)

@app.route('/intro', methods=['POST'])
def intro_post():
    username = request.form.get('username')
    session['username'] = username  

    userrole = request.form['role']
    session['userrole'] = userrole
    session['scene'] = map.START.urlname
    return redirect(url_for('episode_guide_get')) 


@app.route('/episode_guide', methods=['GET'])
def episode_guide_get():
    thescene = map.SCENES[session['scene']]
    username = session['username']
    userrole = session['userrole']

    return render_template('episode_guide.html', 
                            episodes=map.EPISODES, 
                            name=username, 
                            role=userrole)


@app.route('/select_episode', methods=['GET'])
def select_episode_get():
    url = request.args.get('urlname', '')
    session['scene'] = url
    return redirect(url_for('game_get'))


@app.route('/game', methods=['GET'])
def game_get():
    if 'scene' in session:        
        if session['userrole'] == 'light':
          light = True  
        else:
          light = False 
        thescene = map.SCENES[session['scene']]
        return render_template('show_scene.html', 
                                scene=thescene, 
                                lightside=light,
                                player_health=session['player_health'],
                                enemy_health=session['enemy_health'],
                                health_info = 0)
    else:
# The user doesn't have a session...
# What should your code do in response?
        return render_template('you_died.html')

@app.route('/game', methods=['POST'])
def game_post():
    userinput = request.form.get('userinput')

    if 'scene' in session:
        currentscene = map.SCENES[session['scene']]
        bonus = 0

        if session['userrole'] == 'light':
          light = True  
        else:
          light = False 

        nextscene = currentscene.action(userinput, light)

        if type(nextscene) is int:
          bonus = nextscene
          nextscene = None
          userinput = ""

        if userinput == "" or nextscene is None:                      
          fighter_state = strike(bonus);
          if fighter_state != 0:
            next_scene = map.game_over 
            next_template = 'game_over.html'
          else:
            next_scene = currentscene
            next_template = 'show_scene.html'

          return render_template(next_template, 
                                 scene=next_scene,
                                 lightside=light,
                                 player_health=session['player_health'],
                                 enemy_health=session['enemy_health'],
                                 health_info = bonus)
        else:
          if nextscene == map.sudden_death:
            next_template = 'sudden_death.html'
          elif nextscene == map.victory:
            next_template = 'victory.html'
          else:
            reset_health()
            next_template = 'show_scene.html'

          
            
            #return render_template('sudden_death.html', 
            #                        scene=nextscene,
            #                        lightside=light,
            #                        player_health=session['player_health'],
            #                        enemy_health=session['enemy_health'],
            #                        health_info = bonus)

          session['scene'] = nextscene.urlname
          return render_template(next_template, 
                                  scene=nextscene,
                                  lightside=light,
                                  player_health=session['player_health'],
                                  enemy_health=session['enemy_health'],
                                  health_info = bonus)
    else:
        # There's no session, how could the user get here?
        # What should your code do in response?
        return render_template('you_died.html')

# This URL initializes the session with starting values
@app.route('/')
def index():
    session['scene'] = map.INTRO.urlname
    return redirect(url_for('intro_get')) # redirect the browser to the url for game_get

app.secret_key = 'replace this with your secret key'

if __name__ == "__main__":
    app.run()
