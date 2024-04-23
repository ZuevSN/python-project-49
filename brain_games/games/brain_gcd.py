from brain_games.scripts import question_machine


def main():
    game_text = 'Find the greatest common divisor of given numbers.'
    questions = ('gcd',)
    question_machine.respondent(game_text, questions)


if __name__ == "__main__":
    main()
