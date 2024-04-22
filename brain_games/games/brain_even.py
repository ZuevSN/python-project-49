from brain_games.scripts import question_machine


def main():
    question_machine.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    questions = ('even',)
    question_machine.spinner(questions)


if __name__ == "__main__":
    main()
