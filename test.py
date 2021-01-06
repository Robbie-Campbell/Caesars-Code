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
    bgcolor("black")
    speed(30)
    index = 0
    for i in range(765):
        if i % 2 == 0:
            left(91)
            forward(20 + i)
            if i < 247:
                color(252, 247 - i % 247, 135 - (i % 135))
            elif i < 502:
                index += 1
                color(252 - i % 252, index % 255, 23)
            else:
                index += 1
                color(index % 255, 255 - index % 255, 23 + index % 232)


def square_a_number_in_the_parameter(number_to_be_squared):
    return number_to_be_squared * number_to_be_squared


def black_star():
    colormode(255)
    speed(50)
    width(3)
    for i in range(500):
        color(i % 255, i % 255, i % 255)
        left(129)
        forward(501 - i)
        if i % 2 == 0:
            penup()
            left(3)
            pendown()
    Screen().exitonclick()


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
    
    
def is_a_vowel(word):
    vowels = "aeiou"
    if vowels.__contains__(word[0].lower()):
        return word + " starts with a vowel"
    else:
        return word + " starts with a consonant"


def how_many_vowels(phrase):
    vowels = "aeiou"
    vowel_count = 0
    consonant_count = 0
    for letter in phrase:
        if vowels.__contains__(letter):
            vowel_count += 1
        else:
            consonant_count += 1
    return "There are " + str(vowel_count) + " vowels in the given phrase and " + str(consonant_count) + " consonants."


def split_on_first_vowel(phrase):
    vowels = "aeiou"
    separated = list(phrase)
    for index, letter in enumerate(separated):
        if vowels.__contains__(letter):
            return ''.join(separated[index:])
    return "No vowels in phrase"


if __name__ == "__main__":
    for key in caesars_code():
        print(key, caesars_code().get(key))
    pretty()
    print(square_a_number_in_the_parameter(50))

    print(is_a_vowel("what"))
    print(how_many_vowels("That's a good sentence joe"))
    print(split_on_first_vowel("brilliant"))

    
