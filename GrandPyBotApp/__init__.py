import os
from flask import Flask

from GrandPyBotApp.views import app
from GrandPyBotApp import models


@app.cli.command()
def init_db():
    models.init_db()
