import string
from random import randint
from turtle import *

#
# def fizzbuzzer(number):
#     if number % 3 == 0 and number % 5 == 0:
#         return "fizzbuzz"
#     elif number % 5 == 0:
#         return "buzz"
#     elif number % 3 == 0:
#         return "fizz"
#     else:
#         return number


def get_full_alphabet():
    alphabet = []
    for letter in string.ascii_lowercase:
        alphabet += letter
    return alphabet


def caesars_code():
    encrypt = get_full_alphabet()
    new_alphabet = []
    encrypted_values_pair = {}
    for value in range(len(encrypt)):
        new_alphabet += encrypt[value - 3]
        encrypted_values_pair[value] = new_alphabet[value]
    return encrypted_values_pair


def pretty():
    colormode(255)
    speed(30)
    for i in range(765):
        if i % 2 == 0:
            left(91)
            forward(20 + i)
            if i < 255:
                color(i % 255, 0, 0)
            elif i < 510:
                color(0, i % 255, 0)
            else:
                color(0, 0, i % 255)
def o():
    color("black")
    for i in range(4):
        if i % 2 == 0:
            forward(50)
            left(90)
        else:
            forward(100)
            left(90)
    forward(50)


def c():
    color("pink")
    forward(50)
    left(180)
    forward(50)
    right(90)
    forward(100)
    right(90)
    forward(50)
    color("white")
    forward(5)
    right(90)
    forward(100)
    left(90)


def l():
    color("black")
    forward(50)
    left(180)
    forward(50)
    right(90)
    forward(100)
    left(180)
    forward(100)
    left(90)
    forward(50)


def white_space():
    color("white")
    forward(50)


if __name__ == "__main__":
    # for key in caesars_code():
    #     print(key, caesars_code().get(key))
    pretty()

