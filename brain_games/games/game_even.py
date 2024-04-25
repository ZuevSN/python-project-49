import random

MAIN_QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        result = True
    else:
        result = False
    return result


def get_right_answer_and_question():
    number = random.randint(1, 100)
    if is_even(number):
        result = 'yes'
    else:
        result = 'no'
    return result, number
