first_choice = input("Welcome, into a journey, to start you have to write, "
                     "which way you wanna go, 'left' or 'right'? ").lower()

if first_choice == "left":
    second_choice = input("Good job,\n next step do you wanna 'wait' for boat or 'swim' across the ocean: ").lower()
    if second_choice == "wait":
        third_choice = input("the next is which door do you wanna go: 'red', 'blue', 'yellow'?: ").lower()
        if third_choice == "yellow":
            print("Congrats. You found the treasure!!!")
        else:
            print("game over")
    else:
        print("game over")
else:
    print("game over")

