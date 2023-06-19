import string
import random

lowerCase = list(string.ascii_lowercase)
upperCase = list(string.ascii_uppercase)
numbers = list(string.digits)
symbols = list(string.punctuation)


def getInput():
    return input().lower()


def mistake():
    print("To generate password - write '(E)asy', '(M)edium' or '(H)ard' and desirable length(up to 30) e.g. 'e 12' - easy password with 12 symbols\nType 'exit' to exit the programm")


def lowergen(password):
    list_of_lower = random.sample(lowerCase, random.randint(0, 4))
    password += list_of_lower
    return password


def uppergen(password):
    list_of_upper = random.sample(upperCase, random.randint(0, 4))
    password += list_of_upper
    return password


def numbergen(password):
    list_of_numbers = random.sample(numbers, random.randint(0, 4))
    password += list_of_numbers
    return password


def symbolgen(password):
    list_of_symbols = random.sample(symbols, random.randint(0, 4))
    password += list_of_symbols
    return password


def easyPass(length):
    while len(password) < int(length):
        rand = random.randint(1, 2)
        if rand == 1:
            lowergen(password)
        elif rand == 2:
            numbergen(password)
    return password[0:length]


def medPass(length):
    while len(password) < int(length):
        rand = random.randint(1, 3)
        if rand == 1:
            lowergen(password)
        elif rand == 2:
            uppergen(password)
        elif rand == 3:
            numbergen(password)
    return password[0:length]


def hardPass(length):
    while len(password) < int(length):
        rand = random.randint(1, 4)
        if rand == 1:
            lowergen(password)
        elif rand == 2:
            uppergen(password)
        elif rand == 3:
            numbergen(password)
        elif rand == 4:
            symbolgen(password)
    return password[0:length]


def printpass(letter, number):
    number = int(number)
    if number not in range(1, 31) or number > 30 or number < 1:
        return mistake()
    if letter == "easy" or letter == "e":
        print(
            f"Your password is {''.join(easyPass(number))}\nType 'exit' to exit the programm")
    elif letter == "medium" or letter == "m":
        print(
            f"Your password is {''.join(medPass(number))}\nType 'exit' to exit the programm")
    elif letter == "hard" or letter == "h":
        print(
            f"Your password is {''.join(hardPass(number))}\nType 'exit' to exit the programm")
    else:
        return mistake()


print("""How difficult your password should be:
(E)asy?
(M)edium?
(H)ard?

How long your password should be?(up to 30)
Write (difficulty length)
e.g. 'e 12' - easy password with 12 symbols""")


while True:
    password = []
    userInput = getInput()
    if userInput == 'exit':
        print("You're welcome")
        break
    ui = userInput.split(' ')
    if len(ui) == 2:
        if ui[1].isdigit():
            printpass(ui[0], ui[1])
        else:
            mistake()
    else:
        mistake()
