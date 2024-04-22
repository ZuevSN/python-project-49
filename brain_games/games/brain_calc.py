from brain_games.scripts import question_machine


def main():
    question_machine.welcome_user()
    print('What is the result of the expression?')
    score = 0
    end = False
    questions = ('+', '-', '*')
    while not end:
        score, end = question_machine.respondent(questions, score)


if __name__ == "__main__":
    main()
