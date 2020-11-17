# -*- coding: utf-8 -*-
# ! /usr/bin/env python
"""
Created on 11 november 2020
@author: Anthony THILLEROT
"""

# import here ##
from json import dumps, loads
import GrandPyBotApp.utils_mod.wikiapi as wk

# Class here ##

WK = wk.WikiApi()


def test_search_page_on_wikipedia(requests_mock):
    """
       this method is the test of method search_page_on_wikipedia of class WikiApi
       :type requests_mock: object mock of the requests library
    """
    result = dumps({'query':
                        {'search': [{'title': 'hahaha',
                                     'pageid': "123ici"}]
                         }})

    requests_mock.get(url=WK.wiki_url, text=result)

    assert WK.search_page_on_wikipedia("test") == loads(result)['query']['search']


def test_get_resume_search(requests_mock):
    """
    this method is the test of method get_resume_search of class WikiApi
    :type requests_mock: object mock of the requests library
    """
    sentences = "La tour Eiffel est une tour de fer puddlé de 324 mètres de hauteur " \
                "(avec antennes) située à Paris, à l’extrémité nord-ouest du parc du " \
                "Champ-de-Mars en bordure de la Seine dans le 7e arrondissement. " \
                "Son adresse officielle est 5, avenue Anatole-France. Construite en " \
                "deux ans par Gustave Eiffel et ses collaborateurs our l’Exposition universelle " \
                "de Paris de 1889, et initialement nommée « tour de 300 mètres »"

    result = dumps({'query': {'pages': {"123ici": {"extract": sentences}}}})

    requests_mock.get(url=WK.wiki_url, text=result)
    dict_s = {'title': 'hahaha', 'pageid': '123ici'}

    assert WK.get_resume_search(dict_s) == sentences
