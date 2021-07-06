def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    answer_1 = float(input("Write your First number: "))

    continuing = "y"
    while continuing == "y":

        num1 = answer_1
        num2 = float(input("Write your number: "))
        print(" +\n -\n *\n /\n")
        input_operation = input("Pick your operator from above: ")

        answer_1 = operators[input_operation](num1, num2)
        print(f"{num1} {input_operation} {num2} = {answer_1}")

        continuing = input("Do you want to continue? Type 'Y' or 'N' for reset or B for break: ").lower()
        if continuing == "n":
            calculator()
            break


calculator()
