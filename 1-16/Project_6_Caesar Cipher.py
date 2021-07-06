import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            ' ', ',', '.', '/', '?', ';', ':', '_'
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            '!', '#', '$', '%', '&', '(', ')', '*', '+', '=', '-', '"', '@']
random.Random(645).shuffle(alphabet)


def caesar(input_text, shift_number, directed):
    encrypted = ''

    if directed == "decode":
        shift_number *= -1

    for char in input_text:
        if char in alphabet:
            char_index = alphabet.index(char) + shift_number
            encrypted += alphabet[char_index]
        else:
            encrypted += char

        if 100 > char_index > 55:
            char_index -= 56
        elif char_index < 0:
            char_index += 56
        elif char_index > 100:
            print("Error, number is too big")
            break

    if directed == "encode":
        print("Your Encrypt Massage:\n" + encrypted)
    elif directed == "decode":
        print("Your Decrypt Massage:\n" + encrypted)


repeat_input = "yes"
while repeat_input == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message, but some symbols may not working:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(input_text=text, shift_number=shift, directed=direction)
    repeat_input = input("Do you wanna Repeat? Yes or No? \n").lower()
    if repeat_input != "yes":
        break
