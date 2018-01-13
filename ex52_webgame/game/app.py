from flask import Flask, session, request
from flask import url_for, redirect, render_template
import map

app = Flask(__name__)


@app.route('/intro', methods=['GET'])
def intro_get():    
    thescene = map.SCENES[session['scene']]
    return render_template('intro.html', scene=thescene)

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
    return render_template('episode_guide.html', episodes=map.EPISODES , name=username, role=userrole)


@app.route('/select_episode', methods=['GET'])
def select_episode_get():
    url = request.args.get('urlname', '')
    session['scene'] = url
    return redirect(url_for('game_get'))


@app.route('/game', methods=['GET'])
def game_get():
    if 'scene' in session:
        thescene = map.SCENES[session['scene']]
        return render_template('show_scene.html', scene=thescene)
    else:
# The user doesn't have a session...
# What should your code do in response?
        return render_template('you_died.html')

@app.route('/game', methods=['POST'])
def game_post():
    userinput = request.form.get('userinput')
    if 'scene' in session:
        if userinput is None:
            # Weird, a POST request to /game with no user input... what should your code do?
            return render_template('you_died.html')
        else:
            currentscene = map.SCENES[session['scene']]
            nextscene = currentscene.go(userinput)
            if nextscene is None:
                # There's no transition for that user input.
                # what should your code do in response?
                return render_template('you_died.html')
            else:
                session['scene'] = nextscene.urlname
                return render_template('show_scene.html', scene=nextscene)
    else:
        # There's no session, how could the user get here?
        # What should your code do in response?
        return render_template('you_died.html')

# This URL initializes the session with starting values
@app.route('/')
def index():
    session['scene'] = map.INTRO.urlname
    session['username'] = None
    session['userrole'] = None
    return redirect(url_for('intro_get')) # redirect the browser to the url for game_get

app.secret_key = 'replace this with your secret key'

if __name__ == "__main__":
    app.run()
