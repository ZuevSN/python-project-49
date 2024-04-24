import random
import math

MAIN_QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def isprime(number):
    string = str(number)
    result = 'yes'
    if number == 1:
        result = 'no'
    for value in range(2, int(math.sqrt(number)) + 1):
        if number % value == 0:
            result = 'no'
            break
    return result, string


def game_arguments():
    number = random.randint(1, 50)
    return isprime(number)
