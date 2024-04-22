from brain_games.scripts import question_machine


def main():
    question_machine.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    score = 0
    end = False
    questions = ('even',)
    while not end:
        score, end = question_machine.respondent(questions, score)


if __name__ == "__main__":
    main()
