import requests
import re


def upload_pass_base(fp):
    r = requests.get(fp)
    return r.text


# checking passwords for the presence of spaces and tabs
def input_correct_password():
    FOUR_SYMBOLS = 4
    password = ''
    while ((' ' in password) or len(password)) < FOUR_SYMBOLS:
        print("Uncorrect input: using spaces or less then 4 symbols ")
        password = input('Input your password:\n')
        return None
    return password


def get_password_strength(password):
    points = 0
    RECOMMENDED_PASSWORD_LENGTH = 14
    base = upload_pass_base('https://beastrock.github.io/blackpass.txt')
    # inclusion from the base of bad passwords
    if password in base:
        return print("Your password is in the base of bad passwords:\n"
                     "it is weak like a boxer after 10 rounds\n"
                     "password power: 1/10")
    if len(re.findall(password, base)) >= 1:
        print("password includes one or more words from  blacklist: +0 point")
    else:
        points += 2
        print("password isn't in bad passwords base: +2 points")
    # inclusion of special characters
    if re.search("[\W\s]", password):
        points += 2
        print("included special characters: +2 points")
    else:
        print("no special characters: 0 points")
    # the use of both upper-case and lower-case letters (case sensitivity)
    if password.islower() or password.isupper():
        print('only one case is used: 0 points')
    else:
        points += 2
        print('two cases are used: +2 points')
    # estimating password length
    if len(password) >= RECOMMENDED_PASSWORD_LENGTH:
        points += 2
        print('long password length: +2 points')
    elif len(password) < (RECOMMENDED_PASSWORD_LENGTH / 2):
        print('short password length: 0 points')
    else:
        points += 1
        print('medium password length: +1 point')
    # inclusion of one or more numerical digits
    if len(re.findall("[\d]", password)) == (len(password)):
        print("password includes only digits: 0 points")
    elif (len(re.findall("[\d]", password))) == 1:
        points += 1
        print("includes one digit: 1 point")
    elif (len(re.findall("[\d]", password))) > 1:
        points += 2
        print("includes one or more digits: +2 points")
    elif (len(re.findall("[\d]", password))) == 0:
        print("no digits: 0 points")

    message = 'Your password strength, is {}/10!'.format(points)
    print(message)
    return None


if __name__ == '__main__':
    get_password_strength(input_correct_password())
