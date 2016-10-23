import requests
import re


def upload_pass_base(fp):
    r = requests.get(fp)
    return r.text


def input_password():
    password = input('Input password:\n')
    while ' ' in password:
        password = input('Spaces aren\'t allowed. Input correct password :\n')
    print(password)
    return password


def get_password_strength(password):
    password_strength = 0
    points = 0
    RECOMMENDED_PASSWORD_LENGTH = 14
    FIVE_SYMBOLS = 5
    # recommended length
    if len(password) >= RECOMMENDED_PASSWORD_LENGTH:
        length = 2
    elif (RECOMMENDED_PASSWORD_LENGTH * 0.5) <= len(password) < RECOMMENDED_PASSWORD_LENGTH:
        length = 1
    elif FIVE_SYMBOLS < len(password) < (RECOMMENDED_PASSWORD_LENGTH * 0.5):
        length = 0

    # inclusion of special characters
    if re.search("[\W\s]", password):
        special_characters = 2
    else:
        special_characters = 0
    # the use of both upper-case and lower-case letters (case sensitivity)
    if not (password.islower() or password.isupper()):
        case_sensitive = 2
    else:
        case_sensitive = 1

    return length, being_in_base, case_sensitive, special_characters, digits


def print_result(length=0, being_in_base=0, case_sensitive=0, special_characters=0, digits=0):
    #
    if length == 2:
        print('long password length: +2 points')
    elif length == 1:
        print('medium password length: +1 point')
    elif length == 0:
        print('short password length: 0 points')
    elif length == -1:
        print('Very short password: 1/10 ')
    #
    if being_in_base == 2:
        print("password isn't in bad passwords base: +2 points")
    elif being_in_base == 0:
        print("Password is in the base of bad passwords.\n"
              "it is weak like a boxer after 10 rounds: 1/10\n")
    #
    if digits == 2:
        print("includes one or more digits: +2 points")
    elif digits == 0:
        print("no digits: 0 points")
    elif digits == 1:
        print("includes one digit: 1 point")
    elif digits == -1:
        print("Password have to include letters: 1/10")
    #
    if special_characters == 2:
        print("included special characters: +2 points")
    elif special_characters == 0:
        print("no special characters: 0 points")

    if case_sensitive == 2:
        print('two cases are used: +2 points')
    elif case_sensitive == 0:
        print('only one case is used: 0 points')

    password_strength = sum(length, being_in_base, case_sensitive,
                            special_characters, digits)
    message = 'Your password strength, is {}/10!'.format()
    print(message)
    return password_strength


if __name__ == '__main__':
    password = input_password()
    get_password_strength(password)
    print_result(get_password_strength(password))
