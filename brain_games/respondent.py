from brain_games.cli import welcome_user
import prompt

WIN_SCORE = 3


def engine(game):
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print(game.MAIN_QUESTION)
    for _ in range(WIN_SCORE):
        result, string = game.get_right_answer_and_question()
        print(f'Question: {string}')
        answer = prompt.string('Your answer: ')
        if str(answer).lower() != str(result):
            print(f'''\'{answer}\' is wrong answer ;(. \
Correct answer was \'{result}\'
Let\'s try again, {name}!''')
            return
        print("Correct!")
    print(f"Congratulations, {name}!")
