import random
import math

MAIN_QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number == 1:
        return False
    for value in range(2, int(math.sqrt(number)) + 1):
        if number % value == 0:
            return False
    return True


def get_right_answer_and_question():
    number = random.randint(1, 50)
    result = 'yes' if is_prime(number) else 'no'
    return result, number
