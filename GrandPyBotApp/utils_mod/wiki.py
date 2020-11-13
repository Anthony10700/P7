# -*- coding: utf-8 -*-
# ! /usr/bin/env python
"""
Created on 01 november 2020
@author: Anthony THILLEROT
"""

# import here ##
from difflib import SequenceMatcher
from GrandPyBotApp.utils_mod.wikiapi import WikiApi


# Class here ##


class Wiki:
    """
    This class contains all the objects and all the methods concerning the wikipedia API
    the main method is the get_a_resume
    """

    def __init__(self):
        self.api_wiki = WikiApi()
        self.text_for_research_similar = ""
        self.best_i_similar = 0
        self.page_results_number_max = 10
        self.result = ""
        self.resume_return = ""

    def get_resume_return(self):
        """
        :return: the presentation paragraph on Wikipedia
        """
        return str(self.resume_return)

    def get_a_resume_to_in_var(self, text):
        """
        This method allows from the text that the user to enter to retrieve the presentation
        paragraph on Wikipedia.
        This method also allows to check in case of error which would be returned by the
        Wikipedia API.
        This is why in except, I mainly looped the elements returned by the search to be able to
        display a result to the user
        :param text: the search text that the user to enter
        """

        # try:
        last_similar_best = 0.
        self.best_i_similar = 0

        self.result = self.api_wiki.search_page_on_wikipedia(text)
        if self.result != "request error":

            print(self.result)

            if self.result.__len__() == 1:
                self.resume_return = self.api_wiki.get_resume_search(self.result[0])

            self.text_for_research_similar = text[:]

            for var_i, result_in in enumerate(self.result):
                tmp_similar = self.similar(result_in["title"], self.text_for_research_similar)
                if tmp_similar > last_similar_best:
                    last_similar_best = tmp_similar
                    self.best_i_similar = var_i

            print("best similar : ", self.result[self.best_i_similar])
            self.resume_return = self.api_wiki.get_resume_search(self.result[self.best_i_similar])

    @staticmethod
    def similar(text_a, text_b):
        """
        This method uses the Difflib library with the sequence patcher ratio method
        for to have a correspondence ratio between two strings
        :param text_a: this variable corresponding first text to compare
        :param text_b: this variable corresponds in second text to compare
        :return: the method SequenceMatcher returns a ratio between 0 and 1 which corresponds to the
        similarity between the two sequences
        """

        return SequenceMatcher(None, text_a, text_b).ratio()
