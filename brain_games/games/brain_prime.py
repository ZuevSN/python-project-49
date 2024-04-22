from brain_games.scripts import question_machine


def main():
    question_machine.welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    questions = ('prime',)
    question_machine.spinner(questions)


if __name__ == "__main__":
    main()
