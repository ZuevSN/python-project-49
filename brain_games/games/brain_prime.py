from brain_games.scripts import question_machine


def main():
    question_machine.welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    score = 0
    end = False
    questions = ('prime',)
    while not end:
        score, end = question_machine.respondent(questions, score)


if __name__ == "__main__":
    main()
