import random
import math

MAIN_QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    result = True
    if number == 1:
        result = False
    for value in range(2, int(math.sqrt(number)) + 1):
        if number % value == 0:
            result = False
            break
    return result


def get_right_answer_and_question():
    number = random.randint(1, 50)
    if is_prime(number):
        result = 'yes'
    else:
        result = 'no'
    return result, number
