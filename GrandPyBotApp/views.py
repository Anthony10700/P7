from flask import Flask, render_template, url_for, request
import os

TEMPLATE_DIR = os.path.abspath('GrandPyBotApp/templates')
STATIC_DIR = os.path.abspath('GrandPyBotApp/static')

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')





# To get one variable, tape app.config['MY_VARIABLE']

from GrandPyBotApp.utils import find_content, OpenGraphImage

@app.route('/')
@app.route('/index/')
def index():
    if 'img' in request.args:
        img = request.args['img']
        og_url = url_for('index', img=img, _external=True)
        og_image = url_for('static', filename=img, _external=True)
    else:
        og_url = url_for('index', _external=True)
        
    return render_template('index.html')

