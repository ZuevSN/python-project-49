import prompt
import random
from brain_games.scripts import cli
from brain_games.scripts import brain_even


def progression():
    a1 = random.randint(1, 100)
    step = random.randint(1, 100)
    amount = random.randint(5, 10)
    progression_string = ''
    random_position = random.randint(0, amount - 1)
    # формирую отображаемую строку
    for i in range(0, amount):
        if i == random_position:
            result = a1 + i * step
            progression_string = progression_string + ' ' + '..'
        else:
            progression_string = progression_string + ' ' + str(a1 + i * step)
    print(f'Question:{progression_string}')
    return result


def main():
    name = cli.welcome_user()
    print('What number is missing in the progression?')
    score = 0
    end = False
    while not end:
        result = progression()
        answer = prompt.string('Your answer: ')
        score, end = brain_even.respondent(name, answer, result, score)


if __name__ == "__main__":
    main()