import requests
import pandas as pd
import json
import os

url = "https://api.openweathermap.org/data/2.5/onecall"
api = "API"
MY_LAT = 0
MY_LON = 0


parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": api,
    "units": "metric",
    "exclude": "current,minutely,daily"
    }

res = requests.get(url=url, params=parameters)
res.raise_for_status()
weather_data = res.json()
weather_slice = weather_data["hourly"][7:22]

rain = False
for hour in weather_slice:
    weather_id = hour["weather"][0]["id"]
    if 600 <= int(weather_id) < 700:
        rain = True

if rain:
    print("bring umbrella")

#
#
# with open("weather_data.json", mode="w") as data_file:
#     json.dump(weather_data, data_file, indent=4)
