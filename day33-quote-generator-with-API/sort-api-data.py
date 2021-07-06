from tkinter import *
import text2emotion as te
import random
import requests
import operator
import json
import pandas as pd


def file_operation(new_data):
    try:
        with open("quotes100.json", mode="r") as data_file:
            file = json.load(data_file)
            file.update(new_data)

    except FileNotFoundError:
        with open("quotes100.json", mode="w") as data_file:
            json.dump(new_data, data_file, indent=4)

    else:
        with open("quotes100.json", mode="w") as data_file:
            json.dump(file, data_file, indent=4)


data = requests.get(url="https://type.fit/api/quotes")
data.raise_for_status()
quotes = data.json()


for n in range(len(quotes)):
    text = quotes[n]["text"]
    author = quotes[n]["author"]

    emo = te.get_emotion(text)
    ems = max(emo.items(), key=operator.itemgetter(1))[0]

    if emo[ems] == 0:
        emotion = "Happy"

    profile = {
        f"{n}": {
            "text": text,
            "emotion": ems,
            "percent": emo[ems],
            "author": author
        }
    }
    file_operation(profile)
