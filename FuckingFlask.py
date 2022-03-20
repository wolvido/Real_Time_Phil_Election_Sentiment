from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
from dominate.tags import img
from flask import Flask, render_template, Response

app = Flask(__name__)

def text_export():
    with open('C:\\Users\\Winzyl\\Desktop\\migrate\\filename.csv', 'r') as f:
        return(f.read().splitlines()[-1])

def text_display():
    with open('C:\\Users\\Winzyl\\Desktop\\migrate\\filename.csv', 'r') as f:
        return(f.read())

###############################################

###############################################
#          Define flask app                   #
###############################################
logo = img(src='./static/img/logo.png', height="50", width="100", style="margin-top:-15px")
topbar = Navbar(logo,
                View('Home', 'get_home'),
                View('Percent Positive', 'get_news'),
                View('Tweet Volume', 'get_live'),
                # View('Programme', 'get_programme'),
                # View('Classement', 'get_classement'),
                # View('Contact', 'get_contact'),
                )

# registers the "top" menubar
nav = Nav()
nav.register_element('top', topbar)

app = Flask(__name__)
Bootstrap(app)

###############################################
#          Render Home page                   #
###############################################
@app.route('/', methods=['GET'])
def get_home():
    return(render_template('index.html'))

@app.route('/news', methods=['GET'])
def get_news():
    return(render_template('news.html'))

######################### tweets ###########################
@app.route('/stream')
def stream():
    def generate():
        with open('C:\\Users\\Winzyl\\Desktop\\migrate\\data\\filename.csv') as f:
            while True:
                yield f.read()
                
    return app.response_class(generate(), mimetype='text/plain')

########################## leni ############################
@app.route('/streamLeni')
def streamLeni():
    def generateLeni():
        with open('C:\\Users\\Winzyl\\Desktop\\migrate\\data\\ratio.csv') as f:
            while True:
                yield f.read()
                
    return app.response_class(generateLeni(), mimetype='text/plain')
############################################################

########################## Marcos ############################
@app.route('/streamMarcos')
def streamMarcos():
    def generateMarcos():
        with open('C:\\Users\\Winzyl\\Desktop\\migrate\\data\\marcosRatio.csv') as f:
            while True:
                yield f.read()
                
    return app.response_class(generateMarcos(), mimetype='text/plain')
############################################################

########################## Isko ############################
@app.route('/streamIsko')
def streamIsko():
    def generateIsko():
        with open('C:\\Users\\Winzyl\\Desktop\\migrate\\data\\iskoRatio.csv') as f:
            while True:
                yield f.read()
                
    return app.response_class(generateIsko(), mimetype='text/plain')
############################################################

########################## Ping ############################
@app.route('/streamPing')
def streamPing():
    def generatePing():
        with open('C:\\Users\\Winzyl\\Desktop\\migrate\\data\\lacsonRatio.csv') as f:
            while True:
                yield f.read()
                
    return app.response_class(generatePing(), mimetype='text/plain')
############################################################

########################## Pacman ############################
@app.route('/streamPacman')
def streamPacman():
    def generatePacman():
        with open('C:\\Users\\Winzyl\\Desktop\\migrate\\data\\mannyRatio.csv') as f:
            while True:
                yield f.read()
                
    return app.response_class(generatePacman(), mimetype='text/plain')
############################################################

########################## Tweet Volume #########################

########################## leni ############################
@app.route('/streamLeniVol')
def streamLeniVol():
    def generateLeniVol():
        with open('C:\\Users\\Winzyl\\Desktop\\migrate\\data\\lenSum.csv') as f:
            while True:
                yield f.read()
                
    return app.response_class(generateLeniVol(), mimetype='text/plain')
############################################################

########################## Marcos ############################
@app.route('/streamMarcosVol')
def streamMarcosVol():
    def generateMarcosVol():
        with open('C:\\Users\\Winzyl\\Desktop\\migrate\\data\\marSum.csv') as f:
            while True:
                yield f.read()
                
    return app.response_class(generateMarcosVol(), mimetype='text/plain')
############################################################

########################## Isko ############################
@app.route('/streamIskoVol')
def streamIskoVol():
    def generateIskoVol():
        with open('C:\\Users\\Winzyl\\Desktop\\migrate\\data\\koSum.csv') as f:
            while True:
                yield f.read()
                
    return app.response_class(generateIskoVol(), mimetype='text/plain')
############################################################

########################## Pacman ############################
@app.route('/streamPacmanVol')
def streamPacmanVol():
    def generatePacmanVol():
        with open('C:\\Users\\Winzyl\\Desktop\\migrate\\data\\pacSum.csv') as f:
            while True:
                yield f.read()
                
    return app.response_class(generatePacmanVol(), mimetype='text/plain')
############################################################


###########################################################


###################### date ################################
@app.route('/streamDate')
def streamDate():
    def generateDate():
        with open('C:\\Users\\Winzyl\\Desktop\\migrate\\data\\lenDates.csv') as f:
            while True:
                yield f.read()
                
    return app.response_class(generateDate(), mimetype='text/plain')
############################################################

###############################################
#          Render live page                   #
###############################################
@app.route('/live', methods=["GET"])
def get_live():
    return(render_template('live.html'))

###############################################
#          Render programme page                   #
###############################################
@app.route('/programme', methods=["GET"])
def get_programme():
    return(render_template('programme.html'))

###############################################
#          Render Classement page                   #
###############################################
@app.route('/classement', methods=["GET"])
def get_classement():
    return(render_template('classement.html'))

###############################################
#          Render contact page                   #
###############################################
@app.route('/contact', methods=["GET"])
def get_contact():
    return(render_template('contact.html'))

nav.init_app(app)
####################################################

if __name__ == '__main__':
    app.debug = True
    app.run(threaded=True) #go to http://localhost:5000/ to view the page.