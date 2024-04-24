import prompt


def responde(game, limit=3):
    # 1. Приветствие
    welcome_user()
    # 2. Вопрос игры
    print(game.MAIN_QUESTION)
    # 3. Цикл из задач и ответов
    for i in range(0, limit):
        result, string = game.game_arguments()
        print(f'Question: {string}')
        answer = prompt.string('Your answer: ')
        if answer.lower() == str(result).lower():
            print("Correct!")
        else:
            i = None
            break
    # 4. Результат игры
    result_game(i, answer, result)


def welcome_user():
    print("Welcome to the Brain Games!")
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')


def result_game(x, answer, result):
    if x is None:
        print(f'''\'{answer}\' is wrong answer ;(. \
Correct answer was \'{result}\'
Let\'s try again, {name}!''')
    else:
        print(f"Congratulations, {name}!")
