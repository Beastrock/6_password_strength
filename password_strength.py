import requests
import re


def upload_pass_base(fp):
    r = requests.get(fp)
    return r.text


def input_password():
    password = input('Input password:\n')
    while ' ' in password:
        password = input('Spaces aren\'t allowed. Input correct password :\n')
    return password


def get_password_strength(password):
    RECOMMENDED_PASSWORD_LENGTH = 14
    FIVE_SYMBOLS = 5
    pass_properties = []
    # recommended length
    if len(password) >= RECOMMENDED_PASSWORD_LENGTH:
        length = 2
    elif (RECOMMENDED_PASSWORD_LENGTH * 0.5) <= len(password) < RECOMMENDED_PASSWORD_LENGTH:
        length = 1
    elif FIVE_SYMBOLS < len(password) < (RECOMMENDED_PASSWORD_LENGTH * 0.5):
        length = 0
    else:
        length = -1
    pass_properties.append(length)
    # inclusion from the base of bad passwords
    base = upload_pass_base('https://beastrock.github.io/blackpass.txt')
    if not (password in base):
        being_in_base = 2
    else:
        being_in_base = -1
    pass_properties.append(being_in_base)
    # inclusion of one or more numerical digits
    if (1 < len(re.findall("[\d]", password))) < (len(password)):
        digits = 2
    elif (len(re.findall("[\d]", password))) == 1:
        digits = 1
    elif (len(re.findall("[\d]", password))) == 0:
        digits = 0
    elif len(re.findall("[\d]", password)) == (len(password)):
        digits = -1
    pass_properties.append(digits)
    # inclusion of special characters
    if re.search("[\W\s]", password):
        special_characters = 2
    else:
        special_characters = 0
    pass_properties.append(special_characters)
    # the use of both upper-case and lower-case letters (case sensitivity)
    if not (password.islower() or password.isupper()):
        case_sensitive = 2
    else:
        case_sensitive = 1
    pass_properties.append(case_sensitive)
    return pass_properties


def print_result(pass_properties):
    length = pass_properties[0]
    being_in_base = pass_properties[1]
    digits = pass_properties[2]
    special_characters = pass_properties[3]
    case_sensitive = pass_properties[4]

    if -1 in pass_properties:

    if length == 2:
        print('long password length: +2 points')
    elif length == 1:
        print('medium password length: +1 point')
    elif length == 0:
        print('short password length: 0 points')
    elif length == -1:
        print('Very short password: 1/10 ')
        return None
    #
    if being_in_base == 2:
        print("password isn't in bad passwords base: +2 points")
    elif being_in_base == -1:
        print("Password is in the base of bad passwords.\n"
              "it is weak like a boxer after 10 rounds: 1/10\n")
        return None
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

    password_strength = 1
    message = 'Your password strength, is {}/10!'.format(password_strength)
    print(message)
    return None


if __name__ == '__main__':
    password = input_password()
    result = get_password_strength(password)
    print_result(result)
