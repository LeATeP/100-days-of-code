letters = {
    "A": '.-',
    "B": '-...',
    "C": '-.-.',
    "D": '-..',
    "E": '.',
    "F": '..-.',
    "G": '--.',
    "H": '....',
    "I": '..',
    "J": '.---',
    "K": '-.-',
    "L": '.-..',
    "M": '--',
    "N": '-.',
    "O": '---',
    "P": '.--.',
    "Q": '--.-',
    "R": '.-.',
    "S": '...',
    "T": '-',
    "U": '..-',
    "V": '...-',
    "W": '.--',
    "X": '-..-',
    "Y": '-.--',
    "Z": '--..',

    "SPACE": '/',
}


def convert_str_into_encrypt_str(text, decipher_mode):
    if decipher_mode:
        return decipher_morse_code_into_numbers(text)
    else:
        encrypt = convert_str_into_morse_code(text)
        merge_code = merge_list_into_str(encrypt)
        return merge_code


def convert_str_into_morse_code(text):
    encrypted_list = []
    for word in text:
        if word == " ":
            encrypted_list.append(letters['SPACE'])
        elif word in letters:
            encrypted_list.append(letters[word])
        else:
            pass
    return encrypted_list


def merge_list_into_str(encrypt):
    merged = ''
    for n in encrypt:
        merged += f"{n} "
    return merged


def decipher_morse_code_into_numbers(text):
    decipher = ""
    for n in text.split():
        if n == '/':
            decipher += ' '
        else:
            for word in letters:
                if n == letters[word]:
                    decipher += f"{word}"
    return decipher


def do_you_want_decipher_mode(decipher_mode):
    if decipher_mode == "True":
        return True
    return False
