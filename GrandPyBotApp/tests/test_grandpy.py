"""
Created on 11 november 2020
@author: Anthony THILLEROT
"""

# import here ##

import GrandPyBotApp.utils_mod.grandpy as gp

# Class here ##
GP = gp.GrandPy()


def test_get_text_enter():
    """
    this method is the test of method get_text_enter of class GrandPy
    """
    GP.text_enter = 'anthony'
    tmp_val = GP.get_text_enter
    assert tmp_val == 'anthony'


def test_get_text_exit():
    """
    this method is the test of method get_text_exit of class GrandPy
    """
    GP.text_exit = 'anthony'
    tmp_val = GP.get_text_exit
    assert tmp_val == 'anthony'


def test_get_maps_dict():
    """
    this method is the test of method get_maps_dict of class GrandPy
    """
    GP.maps_dict = 'anthony'
    tmp_val = GP.get_maps_dict
    assert tmp_val == 'anthony'


def test_remove_accents():
    """
    this method is the test of method remove_accents of class GrandPy
    """
    string_base = "anthôny"
    assert GP.remove_accents(string_base) == 'anthony'
