import prompt


def engine(game):
    name = welcome_user()
    print(game.MAIN_QUESTION)
    for i in range(0, 3):
        result, string = game.get_right_answer_and_question()
        print(f'Question: {string}')
        answer = prompt.string('Your answer: ')
        if str(answer).lower() == str(result):
            print("Correct!")
            if i == 2:
                print(f"Congratulations, {name}!")
        else:
            print(f'''\'{answer}\' is wrong answer ;(. \
Correct answer was \'{result}\'
Let\'s try again, {name}!''')
            break


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name
