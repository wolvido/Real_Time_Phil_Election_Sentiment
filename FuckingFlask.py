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

##################################################

###############################################
#          Define flask app                   #
###############################################
logo = img(src='./static/img/logo.png', height="50", width="100", style="margin-top:-15px")
topbar = Navbar(logo,
                View('Home', 'get_home'),
                View('News', 'get_news'),
                View('Live', 'get_live'),
                View('Programme', 'get_programme'),
                View('Classement', 'get_classement'),
                View('Contact', 'get_contact'),
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

#######################################################
@app.route('/stream')
def stream():
    def generate():
        with open('C:\\Users\\Winzyl\\Desktop\\migrate\\filename.csv') as f:
            while True:
                yield f.read()
                

    return app.response_class(generate(), mimetype='text/plain')
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