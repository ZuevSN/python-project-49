import random
import math

MAIN_QUESTION = 'Find the greatest common divisor of given numbers.'


def get_right_answer_and_question():
    x = random.randint(1, 20)
    y = random.randint(1, 20)
    result = math.gcd(x, y)
    string = f'{x} {y}'
    return result, string
