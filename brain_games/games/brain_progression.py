from brain_games.scripts import question_machine


def main():
    question_machine.welcome_user()
    print('What number is missing in the progression?')
    questions = ('progression',)
    question_machine.spinner(questions)


if __name__ == "__main__":
    main()
