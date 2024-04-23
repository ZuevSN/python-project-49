from brain_games.scripts import question_machine


def main():
    game_text = 'What is the result of the expression?'
    questions = ('+', '-', '*')
    question_machine.respondent(game_text, questions)


if __name__ == "__main__":
    main()
