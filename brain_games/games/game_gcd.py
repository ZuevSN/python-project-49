import random
import math

MAIN_QUESTION = 'Find the greatest common divisor of given numbers.'


def game_arguments():
    x = random.randint(1, 20)
    y = random.randint(1, 20)
    result = math.gcd(x, y)
    string = f'{x} {y}'
    return result, string
