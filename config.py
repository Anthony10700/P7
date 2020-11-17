""" CONSTANT of flask and API """
import os
import sys

TEMPLATE_DIR = os.path.abspath('GrandPyBotApp/templates')
STATIC_DIR = os.path.abspath('GrandPyBotApp/static')

if "pytest" in sys.modules:
    KEY_MAPS_PLACES = "YOUR_KEY"
else:
    KEY_MAPS_PLACES = os.environ.get('MAPS_KEY')
