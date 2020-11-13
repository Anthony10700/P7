# -*- coding: utf-8 -*-
# ! /usr/bin/env python
"""
Created on 11 november 2020
@author: Anthony THILLEROT
"""

# import here ##
import GrandPyBotApp.utils_mod.wiki as wk

# Class here ##

WK = wk.Wiki()


def test_similar():
    """
       this method is the test of method similar of class Wiki
    """
    text_a = "BLABLA"
    text_b = "BLAB"
    result = WK.similar(text_a, text_b)
    assert result == 0.8


def test_get_resume_return():
    """
       this method is the test of method get_resume_return of class Wiki
    """
    WK.resume_return = "test"
    return WK.get_resume_return == "test"
