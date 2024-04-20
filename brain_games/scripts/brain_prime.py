import random
import math
from brain_games.scripts import brain_even


def isprime():
    random_numer = random.randint(1, 100)
    result = 'yes'
    for value in range(2, int(math.sqrt(random_numer)) + 1):
        if random_numer % value == 0:
            result = 'no'
            break
    print(f'Question: {random_numer}')
    if random_numer == 1:
        result = 'no'
    return result


def main():
    print("Welcome to the Brain Games!")
    name = brain_even.welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    score = 0
    end = False
    while not end:
        result = isprime()
        score, end = brain_even.respondent(name, result, score)


if __name__ == "__main__":
    main()
