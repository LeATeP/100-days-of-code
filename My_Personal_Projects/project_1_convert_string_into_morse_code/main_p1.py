from library_p1 import convert_str_into_encrypt_str, do_you_want_decipher_mode

decipher_mode = input("Do You want decipher more?: True or False").title()
decipher_mode = do_you_want_decipher_mode(decipher_mode)

string = input("Write your message: ").upper()
x = convert_str_into_encrypt_str(string, decipher_mode)
print(x)


