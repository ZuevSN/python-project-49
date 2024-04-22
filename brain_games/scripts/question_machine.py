import prompt
import random
import math


# Приветствие
def welcome_user():
    print("Welcome to the Brain Games!")
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name


# Функция принимает список вопросов, число успехов и
# ограничитель правильных ответов.
# При обработке: выдает сообщения при успехах и неуспехах;
# Возвращает счет и закончена игра или нет.
def respondent(questions, score: int, limit=3):
    result, string = calculate(questions)
    print(f'Question: {string}')
    answer = prompt.string('Your answer: ')
    if answer.lower() == str(result).lower():
        print("Correct!")
        score += 1
        if score == limit:
            print(f"Congratulations, {name}!")
            end = True
            return score, end
        else:
            end = False
            return score, end
    else:
        print(f'''\'{answer}\' is wrong answer ;(. \
Correct answer was \'{result}\'
Let\'s try again, {name}!''')
        score = 0
        end = True
        return score, end


def calculate(questions):
    # В словаре кортежы из функции, отображения вопроса,
    # списка ограничений для аргументов функции.
    # Список ограничений также определяет количество аргументов функции
    dictionary_questions = {
        '+': (lambda x, y: x + y, lambda x, y: f"{x} + {y}",
              [(10, 100), (10, 100)]),
        'even': (even, None, [(2, 3)]),
        'qrt': (lambda x: x ** 2, lambda x: f"{x}^2", [(2, 10)]),
        '-': (lambda x, y: x - y, lambda x, y: f"{x} - {y}",
              [(10, 100), (10, 100)]),
        '*': (lambda x, y: x * y, lambda x, y: f"{x} * {y}",
              [(1, 10), (1, 10)]),
        '//': (lambda x, y: x // y, lambda x, y: f"{x} // {y}",
               [(1, 100), (1, 100)]),
        '%': (lambda x, y: x % y, lambda x, y: f"{x} % {y}",
              [(1, 100), (1, 100)]),
        '!': (lambda x: math.factorial(x), lambda x: f"{x}!",
              [(2, 5)]),
        'sum_arithm_progr': (sum_arithm_progr,
                             lambda a1, step, amount: f"Арифметическая \
прогрессия. Первый член прогрессии - {a1}, \
разность прогрессии - {step}. Посчитай сумму первых {amount} \
элементов арифмитической прогрессии", [(1, 5), (1, 3), (2, 3)]),
        'gcd': (lambda x, y: math.gcd(x, y), lambda x, y: f"{x} {y}",
                [(1, 100), (1, 100)]),
        'progression': (progression, None,
                        [(1, 100), (1, 100), (5, 10)]),
        'prime': (isprime, None, [(1, 100)]),
    }
    # выбор произвольной операции из пришедших
    random_operation = random.choice(questions)
    question = dictionary_questions[random_operation]
    # генерация аргументов
    args = []
    for limits in question[2]:
        args.append(random.randint(limits[0], limits[1]))
    if question[1] is None:
        result, string = question[0](*args)
    else:
        string = question[1](*args)
        result = question[0](*args)
    # отправка результата и текста для вопроса
    return result, string


# Функции для dictionary_questions
def sum_arithm_progr(a1: int, step: int, amount: int):
    return int((amount * (2 * a1 + step * (amount - 1))) / 2)


def even(x):
    string = str(x)
    if x % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return result, string


def progression(a1, step, amount):
    progression_string = ''
    random_position = random.randint(0, amount - 1)
    # формирую отображаемую строку
    for i in range(0, amount):
        if i == random_position:
            result = a1 + i * step
            progression_string = progression_string + ' ' + '..'
        else:
            progression_string = progression_string + ' ' + str(a1 + i * step)
    string = progression_string[1:]
    return result, string


def isprime(x):
    string = str(x)
    result = 'yes'
    if x == 1:
        result = 'no'
    for value in range(2, int(math.sqrt(x)) + 1):
        if x % value == 0:
            result = 'no'
            break
    return result, string
