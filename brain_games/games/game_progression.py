import random

MAIN_QUESTION = 'What number is missing in the progression?'


def progression(element, step, amount):
    progression_string = ''
    random_position = random.randint(0, amount - 1)
    # формирую отображаемую строку
    for i in range(0, amount):
        if i == random_position:
            result = element
            progression_string = progression_string + ' ' + '..'
        else:
            progression_string = progression_string + ' ' + str(element)
        element += step
    string = progression_string[1:]
    return result, string


def get_right_answer_and_question():
    element = random.randint(1, 10)
    step = random.randint(1, 10)
    amount = random.randint(5, 10)
    return progression(element, step, amount)
