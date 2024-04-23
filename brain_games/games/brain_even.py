from brain_games.scripts import question_machine


def main():
    game_text = 'Answer "yes" if the number is even, otherwise answer "no".'
    questions = ('even',)
    question_machine.respondent(game_text, questions)


if __name__ == "__main__":
    main()
