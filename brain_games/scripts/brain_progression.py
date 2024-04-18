import prompt
import random
from brain_games.scripts import cli
from brain_games.scripts import brain_even


def progression():
    #   limits = [(1, 100),(1, 100),(5, 10)]
    #       for limits in question[2]:
    #           args.append(random.randint(limits[0], limits[1]))
    a1 = random.randint(1, 100)
    step = random.randint(1, 100)
    amount = random.randint(5, 10)
    progression_string = ''
    random_num = random.randint(0, amount - 1)
    for i in range(0, amount):
        if i == random_num:
            result = a1 + i * step
            progression_string = progression_string + ' ' + '..'
        else:
            progression_string = progression_string + ' ' + str(a1 + i * step)
    print(f'Question: {progression_string}')
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
