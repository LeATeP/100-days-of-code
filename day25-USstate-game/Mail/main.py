repl1 = "[name]"

with open("./Input/Names/invited_names.txt") as data:
    names = data.readlines()

with open("./Input/Letters/starting_letter.txt") as data:
    y = data.read()

for name in names:
    stripped = name.strip()
    y1 = y.replace(repl1, stripped)

    with open(f"./letter{stripped}.txt", mode="w") as data1:
        data1.write(y1)

