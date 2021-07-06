import random


def remaining_guess():
    choice_of_difficulty = input("Do you want 'easy' or 'hard'?: ").lower()
    if choice_of_difficulty == "easy":
        return 10
    else:
        return 5


def lucky_number():
    return random.randint(1, 100)


def user_number():
    return int(input("Make a guess: "))


print("Guess Game, from 1 to 100\n"
      "You got 10 attempts in 'Easy' or 5 in 'Hard'")
continuing_game = "y"

while continuing_game == "y":
    game_won = False
    guess_remaining = remaining_guess()
    lucky_num = lucky_number()

    while not game_won or guess_remaining == 0:
        user_input = user_number()

        if user_input == lucky_num:
            print("You won\n")
            game_won = True
        elif user_input > lucky_num:
            print("\nToo high")
        else:
            print("\nToo low")

        if not game_won:
            guess_remaining -= 1
            print(f"Your have {guess_remaining} attempt left\n")

    continuing_game = input("Do you want to continue? 'y' or 'n': ")

