from brain_games.scripts import question_machine


def main():
    question_machine.welcome_user()
    print('Find the greatest common divisor of given numbers.')
    questions = ('gcd',)
    question_machine.spinner(questions)


if __name__ == "__main__":
    main()
