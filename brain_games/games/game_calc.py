import random

MAIN_QUESTION = 'What number is missing in the progression?'


def game_arguments():
    list_operations = [
        (lambda x, y: x + y, lambda x, y: f"{x} + {y}"),
        (lambda x, y: x - y, lambda x, y: f"{x} - {y}"),
        (lambda x, y: x * y, lambda x, y: f"{x} * {y}")
    ]
    operation = random.choice(list_operations)
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    result = operation[0](x, y)
    string = operation[1](x, y)
    return result, string
