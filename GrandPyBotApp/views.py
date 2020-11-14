"""
flask views file for route http
"""

from json import dumps
from flask import Flask, render_template, request
from config import STATIC_DIR, KEY_MAPS_PLACES, TEMPLATE_DIR
from .utils_mod.grandpy import GrandPy
from .utils_mod.wiki import Wiki
import os

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

app.config.from_object('config')


@app.route('/')
def init_template_index():
    """
    This method allows to return the index.html page to the client who connects to the site
    :return: the index.html page
    """
    return render_template('index.html', key_maps_places=KEY_MAPS_PLACES)


@app.route('/chat/', methods=['POST'])
def chat():
    """
    This method corresponds to listening to an HTTP post request from the website on the url /chat/
    :return: The method returns a Json object containing the data to return to the client
    """
    wiki = None
    grand_py = None

    grand_py = GrandPy(os.path.abspath(os.path.dirname(__file__)))
    wiki = Wiki()

    if request.method == "POST":
        grand_py.set_text_enter(request.json["data"])
        print(grand_py.get_text_enter)

        tmp = grand_py.get_text_enter.strip().split(" ")
        if tmp.__len__() == 1:
            grand_py.set_text_enter("C'est quoi " + tmp[0])

        grand_py.start_response()

        if 'lat' in grand_py.get_maps_dict:
            wiki.get_a_resume_to_in_var(grand_py.text_to_maps)
            grand_py.maps_dict.update({'wiki_text': wiki.get_resume_return()})
            grand_py.maps_dict.update(wiki.result[wiki.best_i_similar])
            # print(json.dumps(grand_py.get_maps_dict()))
            return dumps(grand_py.get_maps_dict)
    return dumps({
        'text': "Je suis désolé, je n'ai pas compris, peut, tu être plus précis ? "
                "N'oublie pas que les lieux commence par des majuscules ! :)"})
