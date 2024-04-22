from brain_games.scripts import question_machine


def main():
    question_machine.welcome_user()
    print('What is the result of the expression?')
    questions = ('+', '-', '*')
    question_machine.spinner(questions)


if __name__ == "__main__":
    main()
