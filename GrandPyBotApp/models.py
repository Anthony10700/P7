import logging as lg
import enum

from GrandPyBotApp.views import app


# Create database connection object


class Gender(enum.Enum):
    female = 0
    male = 1
    other = 2


class Content():

    def __init__(self, description, gender):
        self.description = description
        self.gender = gender


def init_db():

    lg.warning('Database initialized!')
