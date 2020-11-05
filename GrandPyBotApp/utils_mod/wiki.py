# -*- coding: utf-8 -*-
# ! /usr/bin/env python
"""
Created on 01 november 2020
@author: Anthony THILLEROT
"""

# import here ##
from difflib import SequenceMatcher
import wikipedia


# Class here ##


class Wiki:
    """
    This class contains all the objects and all the methods concerning the wikipedia API
    the main method is the get_a_resume
    """

    def __init__(self):
        self.site = ""
        self.page = object
        self.instance_wiki = wikipedia
        self.instance_wiki.set_lang("fr")
        self.text_for_research_similar = ""
        self.best_i_similar = 0
        self.page_results_number_max = 10
        self.result = ""

    def get_a_full_page(self, text):
        """
        This method initialize the page variable with the Wikipedia page method
        :param text: the search text that the user to enter
        :return: the method returns a Wikipedia page object
        """
        self.page = wikipedia.WikipediaPage(text)
        return self.page

    def get_a_resume(self, text):
        """
        This method allows from the text that the user to enter to retrieve the presentation
        paragraph on Wikipedia.
        This method also allows to check in case of error which would be returned by the
        Wikipedia API.
        This is why in except, I mainly looped the elements returned by the search to be able to
        display a result to the user
        :param text: the search text that the user to enter
        :return: the presentation paragraph on Wikipedia or a string = "Nothing here sry"
        """
        try:
            last_similar_best = 0.
            self.best_i_similar = 0

            self.result = self.search_on_wiki(text)
            print(self.result)

            if self.result.__len__() == 1:
                self.get_a_full_page(self.result[0])
                return self.page.summary

            self.text_for_research_similar = text[:]

            for var_i, result_in in enumerate(self.result):
                tmp_similar = self.similar(result_in, self.text_for_research_similar)
                if tmp_similar > last_similar_best:
                    last_similar_best = tmp_similar
                    self.best_i_similar = var_i

            print("best similar : " + self.result[self.best_i_similar])
            self.get_a_full_page(self.result[self.best_i_similar])

            return self.page.summary

        except (wikipedia.exceptions.PageError,
                wikipedia.exceptions.WikipediaException,
                wikipedia.exceptions.HTTPTimeoutError,
                wikipedia.exceptions.DisambiguationError,
                wikipedia.exceptions.RedirectError,
                wikipedia.exceptions.ODD_ERROR_MESSAGE):

            for var_i in range(0, int(self.result.__len__() - 1)):
                try:
                    print(str(var_i) + " try : " + self.result[var_i])
                    self.get_a_full_page(self.result[var_i])

                    break
                except (wikipedia.exceptions.PageError,
                        wikipedia.exceptions.WikipediaException,
                        wikipedia.exceptions.HTTPTimeoutError,
                        wikipedia.exceptions.DisambiguationError,
                        wikipedia.exceptions.RedirectError,
                        wikipedia.exceptions.ODD_ERROR_MESSAGE):

                    print("wikipedia.exceptions {0}".format("wiki.py error"))
                    if var_i == self.result.__len__() - 1:
                        return "Nothing here sry"
            return self.page.summary

    def search_on_wiki(self, text):
        """
        This method allows you to search on Wikipedia
        :param text: this parameter is the text entered by the user
        :return: this method return list of results obtained
        """
        return wikipedia.search(text, self.page_results_number_max)

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


if __name__ == "__main__":
    wi = Wiki()
    list_of_result = wi.search_on_wiki("Egypt")
    print(list_of_result)
