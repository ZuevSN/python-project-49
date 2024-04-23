from brain_games.scripts import question_machine


def main():
    game_text = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    questions = ('prime',)
    question_machine.respondent(game_text, questions)


if __name__ == "__main__":
    main()
