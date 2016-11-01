import requests
import re
import os
import getpass


def upload_pass_base(file_path):
    r = requests.get(file_path)
    return r.text


def input_password():
    password = getpass.getpass(prompt='Input password:\n')
    while ' ' in password:
        password = getpass.getpass(prompt='Spaces are not allowed.'
                                          ' Input correct password :\n')
    return password


def get_password_strength(password):
    RECOMMENDED_LENGTH = 14
    FIVE_SYMBOLS = 5
    pass_properties = {}
    base = upload_pass_base('https://beastrock.github.io/pass_base.txt')
    if not (password in base):
        being_in_base = 2
    else:
        being_in_base = -1
    pass_properties.update({"being in base": being_in_base})
    if len(password) >= RECOMMENDED_LENGTH:
        length = 2
    elif (RECOMMENDED_LENGTH * 0.5) <= len(password) < RECOMMENDED_LENGTH:
        length = 1
    elif FIVE_SYMBOLS < len(password) < (RECOMMENDED_LENGTH * 0.5):
        length = 0
    else:
        length = -1
    pass_properties.update({"length": length})
    if 1 < len(re.findall("[\d]", password)) < (len(password)):
        digits = 2
    elif len(re.findall("[\d]", password)) == 1:
        digits = 1
    elif len(re.findall("[\d]", password)) == 0:
        digits = 0
    elif len(re.findall("[\d]", password)) == len(password):
        digits = -1
    pass_properties.update({"digits": digits})
    if not re.search('[А-Яа-яA-Za-z]', password):
        case_sensitive = -1
    elif password.islower() or password.isupper():
        case_sensitive = 0
    elif not (password.islower() or password.isupper()):
        case_sensitive = 2
    pass_properties.update({"case sensitive": case_sensitive})
    if 0 < len(re.findall("[\W\s]", password)) < len(password):
        special_characters = 2
    elif len(re.findall("[\W\s]", password)) == len(password):
        special_characters = 1
    else:
        special_characters = 0
    pass_properties.update({"special characters": special_characters})

    return pass_properties


def print_result(pass_properties):
    password_strength = 0
    being_in_base = pass_properties["being in base"]
    length = pass_properties["length"]
    digits = pass_properties["digits"]
    case_sensitive = pass_properties["case sensitive"]
    special_characters = pass_properties["special characters"]
    if being_in_base == 2 and length != -1:
        print("password is not in bad passwords base: +2 points")
    elif being_in_base == -1:
        print("Password is in the base of bad passwords.\n"
              "It is weak like a boxer after 10 rounds: 1/10\n")
        return
    if length == 2:
        print('long password length: +2 points')
    elif length == 1:
        print('medium password length: +1 point')
    elif length == 0:
        print('short password length: 0 points')
    elif length == -1:
        print('very short password: 1/10 ')
        return
    if digits == 2:
        print("includes one or more digits: +2 points")
    elif digits == 0:
        print("no digits: 0 points")
    elif digits == 1:
        print("includes one digit: +1 point")
    elif digits == -1:
        print("includes only digits: 0 points ")
    if case_sensitive == 2:
        print('two cases are used: +2 points')
    elif case_sensitive == 0:
        print('only one case is used: 0 points')
    elif case_sensitive == -1:
        print('no letters: 0 points')
    if special_characters == 2:
        print("includes special characters: +2 points")
    elif special_characters == 1:
        print("includes only special characters: +1 point")
    elif special_characters == 0:
        print("no special characters: 0 points")
    for value in pass_properties.values():
        if value > 0:
            password_strength += value
    print('Your password strength: {}/10!'.format(password_strength))
    return


if __name__ == '__main__':
    password = input_password()
    result = get_password_strength(password)
    print_result(result)
