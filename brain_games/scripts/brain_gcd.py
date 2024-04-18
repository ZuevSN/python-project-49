import prompt
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
    name = cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    score = 0
    end = False
    while not end:
        result = nod()
        answer = prompt.string('Your answer: ')
        score, end = brain_even.respondent(name, answer, result, score)


if __name__ == "__main__":
    main()
