from brain_games.scripts import question_machine


def main():
    game_text = 'What number is missing in the progression?'
    questions = ('progression',)
    question_machine.respondent(game_text, questions)


if __name__ == "__main__":
    main()
