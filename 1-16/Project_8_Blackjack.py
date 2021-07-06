import random

player_cards = []
computer_cards = []

player_sum = 0
computer_sum = 0


def random_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def jac_remodel():
    card_count = 0
    for card1 in player_cards:
        if card1 == 11 and player_sum > 21:
            player_cards[card_count] = 1
        card_count += 1


user_continue = input("You want start a game?: 'Y' or 'N'").lower()
while user_continue == "y":
    computer_in_game = True
    player_in_game = True

    player_cards = [random_card(), random_card()]
    player_sum = sum(player_cards)

    computer_cards = [random_card(), random_card()]
    computer_sum = sum(computer_cards)

    while computer_sum < 17:
        computer_cards += [random_card()]
        computer_sum = sum(computer_cards)
        if computer_sum > 21:
            computer_in_game = False

    for card in player_cards:
        if player_sum > 21:
            player_cards[0] = random_card()

    print(f"\nYour desk: {player_cards}, Your score = {player_sum} \n"
          f"Computer First Card: {computer_cards[0]} computer score {computer_sum}\n")

    user_confirmation = "y"
    while user_confirmation == "y":
        user_confirmation = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if user_confirmation == "y":
            player_cards += [random_card()]
            player_sum = sum(player_cards)

            jac_remodel()

            print(f"\nYour desk: {player_cards}, Your score = {player_sum}")

            if player_sum > 21:
                player_in_game = False
                break
            elif player_sum == 21:
                break

    if user_confirmation == "n":
        print(f"Your desk: {player_cards}, Your score = {player_sum}")

    if player_sum < computer_sum <= 21:
        player_in_game = False
        computer_in_game = True
    elif computer_sum < player_sum <= 21:
        player_in_game = True
        computer_in_game = False
    elif player_sum == computer_sum <= 21:
        player_in_game = True
        computer_in_game = True

    if not player_in_game and computer_in_game:
        print(f"Computer cards: {computer_cards}, And Score: {computer_sum}\n"
              f"\nYour lose")
    elif player_in_game and not computer_in_game:
        print(f"Computer cards: {computer_cards}, And Score: {computer_sum}\n"
              f"\nYour Won")
    elif not player_in_game and not computer_in_game:
        print(f"\nComputer cards: {computer_cards}, And Score: {computer_sum}\n"
              f"Game is Even")

    user_continue = input("You want start a game?: 'Y' or 'N'").lower()








