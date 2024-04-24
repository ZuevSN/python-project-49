import random

MAIN_QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def even(number):
    string = str(number)
    if number % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return result, string


def game_arguments():
    number = random.randint(1, 100)
    return even(number)
