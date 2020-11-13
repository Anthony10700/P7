"""
Created on 11 november 2020
@author: Anthony THILLEROT
"""

# import here ##

import GrandPyBotApp.utils_mod.grandpy as gp

# Class here ##
GP = gp.GrandPy()


def test_get_text_enter():
    GP.text_enter = 'anthony'
    tmp_val = GP.get_text_enter
    assert tmp_val == 'anthony'


def test_get_text_exit():
    GP.text_exit = 'anthony'
    tmp_val = GP.get_text_exit
    assert tmp_val == 'anthony'


def test_get_maps_dict():
    GP.maps_dict = 'anthony'
    tmp_val = GP.get_maps_dict
    assert tmp_val == 'anthony'


def test_remove_accents():
    string_base = "anthôny"
    assert GP.remove_accents(string_base) == 'anthony'
