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
    text_a = "BLABLA"
    text_b = "BLAB"
    result = WK.similar(text_a, text_b)
    assert result == 0.8


def test_get_resume_return():
    WK.resume_return = "test"
    return WK.get_resume_return == "test"
