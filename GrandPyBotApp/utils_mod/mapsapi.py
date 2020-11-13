# -*- coding: utf-8 -*-
# ! /usr/bin/env python
"""
Created on 07 november 2020
@author: Anthony THILLEROT
"""

# import here ##
from requests import get
from config import KEY_MAPS_PLACES


# Class here ##


class MapsApi:
    """
    This class allows you to call the Google Maps API with requests

    """

    def __init__(self):
        self.base_url = "https://maps.googleapis.com/maps/api/"
        self.key_places = KEY_MAPS_PLACES
        self.places_autocomplete = "place/queryautocomplete/"
        self.places_details = "place/details/"
        self.places_types = "geocode"
        self.list_of_dict_return = []

    @staticmethod
    def request_to_maps(base_url, places, my_param):
        """
        This method allows to retrieve a request from URL

        :param base_url: base url of maps API
        :type base_url: String
        :param places: path of API
        :type places: String
        :param my_param: param of API for ex : {'key':"My_API_KEY",'input': 'string_search'}
        :type my_param: dict of API param
        :return: requests object
        """

        return get(base_url + places + 'json', params=my_param)

    def search_places(self, string_search):
        """
        This method allows you to search for a place

        :param string_search: the text to search
        :type string_search: string
        :return: list of dictionary result [{}]
        """
        my_param = {'input': string_search, 'types': self.places_types, 'language': 'fr',
                    'key': self.key_places}

        my_request = self.request_to_maps(self.base_url, self.places_autocomplete, my_param)

        self.list_of_dict_return = my_request.json()["predictions"]
        return self.list_of_dict_return

    def get_lat_and_lng(self, places_id):
        """
        this method allows to recover the longitude and the latitude I have a place in
        particular according to places_id
        :param places_id: the places_id of the place
        :type places_id: string
        :return: this method returns a dictionary with two keys 'lat' and 'lng'
        """

        my_param = {'place_id': places_id, 'key': self.key_places}
        my_request = self.request_to_maps(self.base_url, self.places_details, my_param)

        result = my_request.json()

        if 200 >= my_request.status_code < 300:
            if result != "Error":
                result = result["result"]["geometry"]["location"]
                result["lat"] = round(result['lat'], 6)
                result["lng"] = round(result['lng'], 6)
                return result

        return {}
