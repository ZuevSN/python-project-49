import prompt
import random
import math


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name


def dialog(answer, result, attempt=3):
    print("victory or fail")


def sum_arithm_progr(arg1, step, amount):
    return int((amount*(2*arg1 + step*(amount - 1)))/2)


def calc():  
#   В списке кортежы из функции, отображения функции , 
#   списка ограничений для аргументов функции(он же определяет количество аргументов функции)
    tuple_operations = [
        (lambda arg1,arg2:    arg1 + arg2,        lambda arg1,arg2:   f"{arg1} + {arg2}", [100,100]), 
        (lambda arg1,arg2:    arg1 - arg2,        lambda arg1,arg2:   f"{arg1} - {arg2}", [100,100]),
        (lambda arg1,arg2:    arg1 * arg2,        lambda arg1,arg2:   f"{arg1} * {arg2}", [10,10]),
        (lambda arg1,arg2:    arg1 // arg2,       lambda arg1,arg2:   f"{arg1} // {arg2}",[100,100]),
        (lambda arg1,arg2:    arg1 % arg2,        lambda arg1,arg2:   f"{arg1} % {arg2}", [100,100]),
        (lambda arg1:    arg1 ** 2,               lambda arg1:        f"{arg1}^2",        [10]),
        (lambda arg1:    math.factorial(arg1),    lambda arg1:        f"{arg1}!",         [5]),
        (sum_arithm_progr,                        lambda arg1, step, amount:f"первый член прогрессии - {arg1},разность прогрессии - {step}.Посчитай сумму первых {amount} элементов арифмитической прогрессии",[5,5,3])     
    ]
    operation = random.choice(tuple_operations)
    args = []
    for item in operation[2]:
        args.append(random.randint(1, item))
    print(f"Реши пример: {operation[1](*args)}")
    print(f"Правильный ответ: {operation[0](*args)}")



def main():
    print("Пример и результат")
#    welcome_user()
    calc()


if __name__ == "__main__":
    main()