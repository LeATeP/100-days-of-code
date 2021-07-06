def number_checker(number):
    not_prime = False
    for numb in range(2, 10):
        if number % numb == 0 and numb is not number:
            not_prime = True
            break

    if not_prime is not True:
        print(f"Number is prime {number}")
    else:
        print(f"Number is not Prime {number}")


user_input = int(input("Check Prime Number or Not: "))
number_checker(user_input)

