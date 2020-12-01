# -*- coding: utf-8 -*-
# ! /usr/bin/env python
"""
Created on 07 november 2020
@author: Anthony THILLEROT
"""

# import here ##
from requests import get


# Class here ##


class WikiApi:
    """
    this class allows you to contact Wikipedia  API
    :param language: the language searches on the site
    :type language: string(2)
    """

    def __init__(self, language="fr"):
        self.base_url = "https://www.mediawiki.org/w/api.php"
        self.wiki_url = ""
        self.list_of_result_search_text = []
        self.__set_lang(language)

    def __set_lang(self, prefix):
        """
        it is a method used to initialize variable wiki_url with the language prefix
        :param prefix: 2 char https://fr.wikipedia.org/wiki/Liste_des_codes_ISO_639-1
        :type prefix: string(2)
        """
        self.wiki_url = 'https://' + prefix.lower() + '.wikipedia.org/w/api.php'

    def search_page_on_wikipedia(self, search_text):
        """
        this method allows you to search for a page on Wikipedia
        :param search_text: search text on Wikipedia
        :type search_text: string
        :return: list of dictionnary with 2 key title and pageid or "request error"
        """
        my_param = {"action": "query",
                    "format": "json",
                    "list": "search",
                    "srsearch": search_text,
                    "srlimit": 11}

        my_request = get(self.wiki_url, params=my_param)

        if 200 >= my_request.status_code < 300:
            self.list_of_result_search_text = my_request.json()['query']['search']
            my_list = []
            for item in self.list_of_result_search_text:
                my_list.append({"title": item["title"], "pageid": item["pageid"]})

            return my_list

        return "request error"

    def __get_summary_content_of_page(self, title, page_id):
        """
        this method allows you to retrieve the first three sentences of the Wikipedia page in
        question
        :param title: title of page
        :type title: string
        :param page_id: id of page
        :type page_id: string
        :return: list of sentences of the Wikipedia page (string) or "request error"
        """
        page_id = str(page_id)  # convert page_id int on str
        my_param = {"action": "query",
                    "titles": title,
                    "prop": "extracts",
                    "explaintext": '',
                    "format": "json"
                    }  # Les paramètres de la requête http

        my_request = get(self.wiki_url, params=my_param)  # Envoyer la requette http get a url wiki url et les paramètres my_param.

        if 200 >= my_request.status_code < 300:  # Cette condition vérifie si la requette c'est bien passer.
            return my_request.json()["query"]["pages"][page_id]["extract"].split("\n")[0:3]  # return les 3 premières phrase de la page wiki.

        return "request error"  # return "request error" si my_request renvoie une erreur.

    def get_resume_search(self, dict_re_search):
        """
        this method allows you to retrieve the first three sentences of the
        Wikipedia page in question

        :param dict_re_search: search_page_on_wikipedia
        :type dict_re_search: list of dictionnary with 2 key title and pageid or "request error"
        :return: three sentences of the Wikipedia page (string) or "request error"
        """
        page_tmp = self.__get_summary_content_of_page(dict_re_search["title"],
                                                      dict_re_search["pageid"])

        if page_tmp != "request error":
            if len(page_tmp) >= 3:
                return page_tmp[0] + "\n" + page_tmp[1] + "\n" + page_tmp[2]
            if len(page_tmp) == 2:
                return page_tmp[0] + "\n" + page_tmp[1]

            return page_tmp[0]

        return "request error"
