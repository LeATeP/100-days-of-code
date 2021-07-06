import requests
from datetime import datetime

MY_LAT = 54.264640
MY_LNG = 52.030820


def is_iss_overhead():

    res = requests.get(url="http://api.open-notify.org/iss-now.json")
    res.raise_for_status()
    data = res.json()

    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT + 5) >= latitude >= (MY_LAT - 5) and (MY_LNG + 5) >= longitude >= (MY_LNG - 5):
        return True
    else:
        print("is not")


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    sun = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    sun.raise_for_status()
    data = sun.json()
    sunrise = float(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = float(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour

    if time_now <= sunrise or time_now >= sunset:
        return True


if is_iss_overhead() and is_dark():
    print("look up")

