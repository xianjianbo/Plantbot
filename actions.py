# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import requests
import sqlite3

class ActionSearchWeather(Action):

    def name(self) -> Text:
        return "action_search_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        loc=tracker.get_slot("location") #从NLU中获取slot
        api_response_gaode=requests.get('https://restapi.amap.com/v3/geocode/geo?address={}&key=5be0cae13eea095cabe6b96c9eda9570'.format(loc))
        api_result_gaode=api_response_gaode.json()
        lat_and_lng=api_result_gaode['geocodes'][0]['location']

        current=requests.get('https://api.caiyunapp.com/v2/ry0vhdhw1KWi9Xik/{}/realtime.json'.format(lat_and_lng)).json()
        temperature_c=current['result']['temperature']
        condition=current['result']['skycon']
       
        dispatcher.utter_message("{}现在是{}，气温{}℃。".format( loc, condition, temperature_c))
        return [SlotSet('location',loc)]

class ActionSearchPlantLocation(Action):

    def name(self) -> Text:
        return "action_search_plant_location"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        plant_name=tracker.get_slot("plant")

        conn = sqlite3.connect('.\\data\\plantdb.db')
        cursor= conn.cursor()
        cur=cursor.execute("select distribution from plant where name='{}'".format(plant_name))
        distribution=cur.fetchone()[0]
        conn.close()

        dispatcher.utter_message("{}有{}。".format(distribution, plant_name))
        return [SlotSet('location',distribution)]