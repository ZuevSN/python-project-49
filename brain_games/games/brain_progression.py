from brain_games.scripts import question_machine


def main():
    question_machine.welcome_user()
    print('What number is missing in the progression?')
    score = 0
    end = False
    questions = ('progression',)
    while not end:
        score, end = question_machine.respondent(questions, score)


if __name__ == "__main__":
    main()
