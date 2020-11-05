import json
import sys
from flask import Flask, render_template, request
import config
from .utils_mod.grandpy import GrandPy
from .utils_mod.wiki import Wiki


app = Flask(__name__, template_folder=config.TEMPLATE_DIR, static_folder=config.STATIC_DIR)

app.config.from_object('config')


@app.route('/')
def init_template_index():
    """
    This method allows to return the index.html page to the client who connects to the site
    :return: the index.html page
    """
    return render_template('index.html', key_maps_places=config.key_maps_places)


@app.route('/chat/', methods=['POST'])
def chat():
    """
    This method corresponds to listening to an HTTP post request from the website on the url /chat/
    :return: The method returns a Json object containing the data to return to the client
    """
    wiki = None
    grand_py = None

    try:
        grand_py = GrandPy()
        wiki = Wiki()
        if request.method == "POST":
            grand_py.set_text_enter(request.json["data"])
            print(grand_py.get_text_enter)
            grand_py.start_response()

            if 'lat' in grand_py.get_maps_dict:
                grand_py.maps_dict.update({'wiki_text': wiki.get_a_resume(grand_py.text_to_maps)})

            # print(json.dumps(grand_py.get_maps_dict()))
            return json.dumps(grand_py.get_maps_dict)

    except (wiki.instance_wiki.exceptions.PageError,
            wiki.instance_wiki.exceptions.WikipediaException,
            wiki.instance_wiki.exceptions.HTTPTimeoutError,
            wiki.instance_wiki.exceptions.DisambiguationError,
            wiki.instance_wiki.exceptions.RedirectError,
            grand_py.inst_gm.exceptions.ApiError, grand_py.inst_gm.exceptions.HTTPError,
            grand_py.inst_gm.exceptions.Timeout, grand_py.inst_gm.exceptions.TransportError):

        print("Error in try chat :", sys.exc_info()[0])
        return json.dumps({
            'text': "Je suis désolé, je n'ai pas compris, peut, tu être plus précis ? N'oublie pas "
                    "que les lieux commence par des majuscules ! :)"})
