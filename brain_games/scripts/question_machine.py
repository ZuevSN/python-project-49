import prompt
import random
import math


# Функция принимает текст игры, список вопросов,
# ограничитель правильных ответов. Возвращает текстовки по игре.
def respondent(game_text: str, questions: list, limit=3):
    # 1. Приветствие
    welcome_user()
    # 2. Вопрос игры
    print(game_text)
    # 3. Цикл из задач и ответов
    for i in range(0, limit):
        result, string = calculate(questions)
        print(f'Question: {string}')
        answer = prompt.string('Your answer: ')
        if answer.lower() == str(result).lower():
            print("Correct!")
        else:
            i = -1
            break
    # 4. Результат
    if i == limit - 1:
        print(f"Congratulations, {name}!")
    else:
        print(f'''\'{answer}\' is wrong answer ;(. \
Correct answer was \'{result}\'
Let\'s try again, {name}!''')


# Приветствие
def welcome_user():
    print("Welcome to the Brain Games!")
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')


# Функция выбирает произвольную функцию из словаря функций
# Исходя из аргументов рассчитывает результат функции и
# выводит текстовку функции
def calculate(questions):
    # 1. Выбор функции
    question = dict_questions[random.choice(questions)]
    # 2. Генерация аргументов для функции
    args = []
    for limits in question[2]:
        args.append(random.randint(limits[0], limits[1]))
    # 3. Вывод результата и текстовки фнукции
    if question[1] is None:
        result, string = question[0](*args)
    else:
        string = question[1](*args)
        result = question[0](*args)
    return result, string


# Функции для словаря функций dict_questions
# Сумма арифмитической прогрессии
def sum_arithm_progr(a1: int, step: int, amount: int):
    result = int((amount * (2 * a1 + step * (amount - 1))) / 2)
    string = f"Арифметическая \
прогрессия. Первый член прогрессии - {a1}, \
разность прогрессии - {step}. Посчитай сумму первых {amount} \
элементов арифмитической прогрессии"
    return result, string


# Чет/нечет
def even(x):
    string = str(x)
    if x % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return result, string


# Недостающий элемент прогрессии
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


# Простое число
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


# В словаре кортежы из функции, отображения вопроса,
# списка ограничений для аргументов функции.
# Список ограничений также определяет количество аргументов функции
dict_questions = {
    '+': (lambda x, y: x + y, lambda x, y: f"{x} + {y}",
          [(10, 100), (10, 100)]),
    'even': (even, None, [(2, 3)]),
    'qrt': (lambda x: x ** 2, lambda x: f"{x}^2", [(2, 10)]),
    '-': (lambda x, y: x - y, lambda x, y: f"{x} - {y}",
          [(10, 100), (10, 100)]),
    '*': (lambda x, y: x * y, lambda x, y: f"{x} * {y}", [(1, 10), (1, 10)]),
    '//': (lambda x, y: x // y, lambda x, y: f"{x} // {y}",
           [(1, 100), (1, 100)]),
    '%': (lambda x, y: x % y, lambda x, y: f"{x} % {y}", [(1, 100), (1, 100)]),
    '!': (lambda x: math.factorial(x), lambda x: f"{x}!", [(2, 5)]),
    'sum_arithm_progr': (sum_arithm_progr, None, [(1, 5), (1, 3), (2, 3)]),
    'gcd': (lambda x, y: math.gcd(x, y), lambda x, y: f"{x} {y}",
            [(1, 100), (1, 100)]),
    'progression': (progression, None, [(1, 100), (1, 100), (5, 10)]),
    'prime': (isprime, None, [(1, 100)])
}
