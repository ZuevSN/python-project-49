import random

MAIN_QUESTION = 'What is the result of the expression?'


def calc(x, y):
    list_operations = [
        (x + y, f"{x} + {y}"),
        (x - y, f"{x} - {y}"),
        (x * y, f"{x} * {y}")
    ]
    operation = random.choice(list_operations)
    result = operation[0]
    string = operation[1]
    return result, string


def get_right_answer_and_question():
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    return calc(x, y)
