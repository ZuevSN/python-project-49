import random

MAIN_QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_right_answer_and_question():
    number = random.randint(1, 100)
    result = 'yes' if is_even(number) else 'no'
    return result, number
