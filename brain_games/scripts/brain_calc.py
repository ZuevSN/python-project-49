import prompt
import random
import math
from brain_games.scripts import cli
from brain_games.scripts import brain_even


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name


def sum_arithm_progr(a1: int, step: int, amount: int):
    return int((amount * (2 * a1 + step * (amount - 1))) / 2)


def calc():
    # В списке кортежы из функции, отображения операции,
    # списка ограничений для аргументов функции.
    # Список ограничений также определяет количество аргументов функции
    tuple_questions = [
        (lambda x, y: x + y, lambda x, y: f"{x} + {y}", [(10, 100), (10, 100)]),
        (lambda x, y: x - y, lambda x, y: f"{x} - {y}", [(10, 100), (10, 100)]),
        (lambda x, y: x * y, lambda x, y: f"{x} * {y}", [(1, 10), (1, 10)]),
        (lambda x, y: x // y, lambda x, y: f"{x} // {y}", [(1, 100), (1, 100)]),
        (lambda x, y: x % y, lambda x, y: f"{x} % {y}", [(1, 100), (1, 100)]),
        (lambda x: x ** 2, lambda x: f"{x}^2", [(2, 10)]),
        (lambda x: math.factorial(x), lambda x: f"{x}!", [(2, 5)]),
        (sum_arithm_progr, lambda a1, step, amount: f"Арифметическая \
прогрессия. Первый член прогрессии - {a1}, \
разность прогрессии - {step}. Посчитай сумму первых {amount} \
элементов арифмитической прогрессии", [(1, 5), (1, 3), (2, 3)]),
    ]
    question = random.choice(tuple_questions)
    args = []
    # генерация аргументов для случайно выбранной функции
    for limits in question[2]:
        args.append(random.randint(limits[0], limits[1]))
    # отправка текстовки примера и результата
    print(f"Question: {question[1](*args)}")
    result = question[0](*args)
    return result


def main():
    name = cli.welcome_user()
    print('What is the result of the expression?')
    attempt = 0
    end = False
    while not end:
        result = calc()
        answer = prompt.string('Your answer: ')
        attempt, end = brain_even.respondent(name, answer, result, attempt)


if __name__ == "__main__":
    main()
