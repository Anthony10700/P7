# -*- coding: utf-8 -*-
# ! /usr/bin/env python
"""
Created on 31 october 2020
@author: Anthony THILLEROT
"""

# import here ##
from json import load
from os import path
from re import sub
from unicodedata import normalize
from GrandPyBotApp.utils_mod.mapsapi import MapsApi
from config import KEY_MAPS_PLACES


# Class here ##


class GrandPy:
    """
    This class concerns Grand Py object
    The main method is start_response it allows to execute several methods in a precise order
    to be able to carry out tasks on the text sent by the user such as for example to remove the
    stop words still the accents the spaces or the conjugation
    """

    def __init__(self, path_or_directory=""):
        self.inst_gm = MapsApi()
        self.text_enter = ""
        self.text_exit = ""
        self.text_temp = []
        self.maps_dict = {}
        self.text_to_maps = ""
        self.google_maps_api_key_places = KEY_MAPS_PLACES
        if path_or_directory == "":
            # regarding this variable i determine if the user to enter a path
            # i saw that an action depending on
            self.path_or_directory = path.dirname(path.realpath('__file__'))
        else:
            self.path_or_directory = path_or_directory

    def set_text_enter(self, phrase):
        """
        This method allows you to assign a value to the variable X
        :param phrase: phrase is the variable at a sign
        :type : string
        """
        self.text_enter = phrase

    @property
    def get_text_enter(self):
        """
        this method allows to recover the variable text_enter
        :return: text_enter
        :type : string
        """
        return self.text_enter

    @property
    def get_text_exit(self):
        """
        this method allows to recover the variable text_exit
        :return: text_exit
        :type : string

        """
        return self.text_exit

    @property
    def get_maps_dict(self):
        """
        this method allows to recover the variable maps_dict
        :return: maps_dict {}
        :type : dict

        """
        return self.maps_dict

    def start_response(self):
        """
        start_response it allows to execute several methods in a precise order
        to be able to carry out tasks on the text sent by the user such as for example to remove the
        stop words still the accents the spaces or the conjugation
        """
        print(self.path_or_directory)
        self.__remove_start_of_sentences()
        self.__stop_by_small_word()
        self.__stop_by_all_word()
        self.__remove_nothing_in_list()
        self.__search_on_maps()
        self.__add_text_to_dict()

    def __add_text_to_dict(self):
        """
        In this method I check if the maps dictionary contains the key lat and if so adds a text
        to the dictionary, and if not adds a text to the dictionary with a phrase "I'm sorry ..."
        """
        if self.__verify_response():
            self.maps_dict.update({
                'text': "Voici ce que j'ai retenu : [ " + self.text_to_maps + " ] Ci-dessous une "
                                                                              "carte maps ou se "
                                                                              "trouve le lieu et "
                                                                              "une petite histoire "
                                                                              "associée. La "
                                                                              "description : "})
        else:
            self.maps_dict.update({
                'text': "Je suis désolé, je n'ai pas compris, peux-tu être plus précis ? "
                        "N'oublie pas que les lieux commence par des majuscules ! :)"})

    def __verify_response(self):
        """I check if the maps dictionary contains the key lat
        :return : bool is the dictionary contains the key lat
        """
        if "lat" in self.maps_dict:
            return True

        return False

    def __stop_by_small_word(self):
        """
            In this method I remove the stop words contained in the stop_by_small_word file
            I also remove the spaces before and after remove the first capital letter of the text
            I also do a regular expression to remove anything that is not letters and numbers
            and I also remove the accents
            :return : this method does not return anything because it performs operations and stocks
            directly in the variables of the class
        """
        with open(
                self.path_or_directory + '/utils_mod/stopwords-json.json', "rb") \
                as json_file:
            data = load(json_file)

        self.text_enter = self.text_enter.strip()
        self.text_enter = self.text_enter[0:1].lower() + self.text_enter[1:]
        self.text_enter = sub(r'[^\w]', ' ', self.text_enter)
        self.text_enter = self.remove_accents(self.text_enter)

        for word_in_data in data:
            word_in_data = " " + self.remove_accents(word_in_data) + " "

            for word in self.text_enter.split(" "):
                word = " " + word + " "
                if word == word_in_data:
                    self.text_enter = self.text_enter.replace(word_in_data, ' ')
        self.text_enter.strip()
        self.text_temp = self.text_enter.split(" ").copy()
        self.text_exit = self.text_enter.split(" ").copy()
        print(self.text_exit)

    def __remove_nothing_in_list(self):
        """
        In this method I remove in a list the elements which contains nothing at all
        This method must be executed after the stop_by_small_word method which it returns a list
        containing words or nothing at all
        """
        tmp = self.text_temp.copy()

        for var_c in range(len(self.text_temp)):
            if self.text_temp[var_c] == '':
                tmp.remove('')
                var_c = 0

        self.text_exit = tmp
        print(tmp)

    def __remove_start_of_sentences(self):
        """
        This method consists in removing the beginning of the user sentence which is always
        the same although the user is not obliged to send it
        """
        self.text_enter = self.text_enter.replace("Que peut tu me dire sur ", '')

    def __search_on_maps(self):
        """
        This method perform a search on google maps Google Maps API according to the number of
        results obtained I loop on the list of results then I return the first occurrence which
        contains the key place_id
        :return : this method does not return anything at all because it updates the dictionary
        maps_dict by adding longitude and latitude as the key then also adds the description of the
        place select
        """

        self.text_to_maps = ' '.join([str(elem) for elem in self.text_exit])

        if self.text_to_maps != "":
            g_place_result = self.inst_gm.search_places(self.text_to_maps)
            print(g_place_result)
            for i in range(len(g_place_result) - 1):
                if "place_id" in g_place_result[i]:
                    image = self.inst_gm.get_lat_and_lng(g_place_result[i]["place_id"])
                    self.maps_dict.update(image)
                    self.maps_dict.update({'name': g_place_result[i]["description"]})
                    print(self.maps_dict)
                    break

    @staticmethod
    def remove_accents(input_str):
        """
        This method consists of removing the accents from the sentence.
        It uses unicodedata library
        :param input_str: input_str is the input value for which the accents will be removed
        :return: The returned value is equal to the input value donate the accents you were removing
        """

        try:
            input_str = input_str.decode("utf-8")
        except (UnicodeDecodeError, AttributeError):
            input_str = input_str
        
        nfkd_form = normalize('NFKD', input_str)
        only_ascii = nfkd_form.encode('ASCII', 'ignore')
        return only_ascii.decode("utf-8")

    def __stop_by_all_word(self):
        """
        This method removes from the sentence a list of words which is saved in a text file.
        :return : this method returns nothing because to the tribe of the class variable value
        """
        print(self.text_enter.split(" "))

        with open(self.path_or_directory + '/utils_mod/liste_francais.txt',
                  "rb") as file_fd:
            lines = file_fd.read().splitlines()

            for word_in_lines in lines:

                word_in_lines = word_in_lines.lower()

                for word in self.text_enter.split(" "):
                    tmp_word = word[:]
                    word = self.remove_accents(word)
                    # word = word.lower()
                    word_in_lines = self.remove_accents(word_in_lines)

                    if word == word_in_lines:
                        self.text_enter = self.text_enter.replace(tmp_word, ' ')

            self.text_enter.strip()
            self.text_temp = self.text_enter.split(" ").copy()
            self.text_exit = self.text_enter.split(" ").copy()
            print(self.text_exit)
