import random
import math
from brain_games.scripts import cli
from brain_games.scripts import brain_even


def nod():
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    print(f'Question: {x} {y}')
    result = math.gcd(x, y)
    return result


def main():
    print("Welcome to the Brain Games!")
    name = cli.welcome_user()
    print('Find the greatest common divisor of given numbers.')
    score = 0
    end = False
    while not end:
        result = nod()
        score, end = brain_even.respondent(name, result, score)


if __name__ == "__main__":
    main()
