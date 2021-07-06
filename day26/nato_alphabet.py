import csv
import pandas

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


# pandas way
data1 = pandas.read_csv("nato.csv")

user = input("write your key: ").upper()
w = {row.letter: row.code for (index, row) in data1.iterrows()}

output = [w[n] for n in user]
print(output)


##########
# standard way
with open("./nato.csv", mode="r") as guess:
    data = csv.reader(guess)
    data3 = [n for n in data]

t = {index: code for index, code in data3}
output2 = [t[n] for n in user]
print(output2)
