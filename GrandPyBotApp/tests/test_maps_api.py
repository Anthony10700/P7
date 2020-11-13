# -*- coding: utf-8 -*-
# ! /usr/bin/env python
"""
Created on 11 november 2020
@author: Anthony THILLEROT
"""

# import here ##
import json
import GrandPyBotApp.utils_mod.mapsapi as mp


# Class here ##

MP = mp.MapsApi()


def test_request_to_maps(requests_mock):
    result = "[{'lat': 54.685278, 'lng': -7.393611}]"
    my_param = {'place_id': "ChIJ59EeF7fRX0gRKo9D7athmJk",
                'key': MP.key_places}

    requests_mock.get(url=MP.base_url + MP.places_details + 'json', text=result)

    assert MP.request_to_maps(MP.base_url, MP.places_details, my_param).text == result


def test_get_lat_and_lng(requests_mock):
    result = json.dumps({'result':
                             {'geometry':
                                  {'location':
                                       {'lat': 54.685278, 'lng': -7.393611}}}})

    requests_mock.get(url=MP.base_url + MP.places_details + 'json', text=result)

    assert MP.get_lat_and_lng("test") == json.loads(result)["result"]["geometry"]["location"]


def test_search_places(requests_mock):
    result = json.dumps({'predictions':
                             [{'description': 'Tour Eiffel, Avenue Anatole France, Paris, France',
                               'matched_substrings': [{'length': 11, 'offset': 0},
                                                      {'length': 5, 'offset': 36}],
                               'place_id': 'ChIJLU7jZClu5kcR4PcOOO6p3I0',
                               'reference': 'ChIJLU7jZClu5kcR4PcOOO6p3I0',
                               'structured_formatting': {'main_text': 'Tour Eiffel',
                                                         'main_text_matched_substrings': [
                                                             {'length': 11, 'offset': 0}],
                                                         'secondary_text': 'Avenue Anatole France,'
                                                                           ' Paris, France',
                                                         'secondary_text_matched_substrings': [
                                                             {'length': 5, 'offset': 23}]},
                               'terms': [{'offset': 0, 'value': 'Tour Eiffel'},
                                         {'offset': 13, 'value': 'Avenue Anatole France'},
                                         {'offset': 36, 'value': 'Paris'},
                                         {'offset': 43, 'value': 'France'}],
                               'types': ['tourist_attraction', 'point_of_interest',
                                         'establishment']}]})

    url = "https://maps.googleapis.com/maps/api/place/queryautocomplete/json?input=test&types=" \
          "geocode&language=fr&key=AIzaSyDlyntwR9xgJCugO56RZP4zSg0xcY1X0Eg"

    requests_mock.get(url=url, text=result)

    assert MP.search_places("test") == json.loads(result)["predictions"]
