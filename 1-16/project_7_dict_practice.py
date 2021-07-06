bets = []

biggest_bet = 0

repeat = "y"
while repeat == "y":
    better = input("Write your name: ")
    price = input("What's your bid?: ")
    price_int = int(price)

    new_bets = {
        "name": better,
        "bet": price_int,
    }

    bets.append(new_bets)

    repeat = input("Like to bet next?, Y or N: ").lower()


for key in bets:
    if key["bet"] > biggest_bet:
        biggest_bet = key["bet"]
        bitter_name = key["name"]

print(f" the biggest bet is {biggest_bet} with {biggest_bet}$")
