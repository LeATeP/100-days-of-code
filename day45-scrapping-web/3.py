from bs4 import BeautifulSoup
import requests


number = 0
score_data = []
id_data = []
title_data = []
link_data = []

response_text = requests.get("https://news.ycombinator.com/news").text

soup = BeautifulSoup(response_text, "html.parser")
all_tr1 = soup.find_all("tr", {"class": "athing"})
for each in all_tr1:
    score = None
    id1 = each["id"]
    score_span = soup.find("span", {"id": f"score_{id1}"})
    storylink = each.find("a", {"class": "storylink"})

    title_data.append(storylink.string)
    link_data.append(storylink['href'])
    id_data.append(id1)

    if score_span is not None:
        score_data.append(int(score_span.string.split()[0]))
    else:
        score_data.append(0)


large = max(score_data)
index = score_data.index(large)
print(title_data[index])
print(link_data[index])








