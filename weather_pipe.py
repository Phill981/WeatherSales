import pandas as pd
import requests
import json
from pprint import pprint 
import pgeocode

def zip_to_city(code, country_code="de"):
    nomi = pgeocode.Nominatim(country_code)
    return nomi.query_postal_code(code)["place_name"]

def kelvin_to_deg(k):
    return str(round(float(k) - 273.15, 2))

def grep_data(zip_code: str):
    api = "7dfd22239ee2fd6ce8a4078d97cc5ff6"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api + "&q=" + zip_code
    req = requests.get(complete_url)
    return kelvin_to_deg(req.json()["main"]["temp"]), req.json()["weather"][0]["description"]


#print(zip_to_city("56410"))