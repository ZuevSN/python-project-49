from brain_games.scripts import question_machine


def main():
    question_machine.welcome_user()
    print('Find the greatest common divisor of given numbers.')
    score = 0
    end = False
    questions = ('gcd',)
    while not end:
        score, end = question_machine.respondent(questions, score)


if __name__ == "__main__":
    main()
