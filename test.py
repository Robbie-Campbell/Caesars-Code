import string

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


if __name__ == "__main__":
    for key in caesars_code():
        print(key, caesars_code().get(key))
