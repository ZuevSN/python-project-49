import prompt
import random
from brain_games.scripts import cli


def even():
    random_number = random.randint(1, 100)
    print(f'Question: {random_number}')
    if random_number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def respondent(name: str, answer: str, result, attempt: int, limit=3):
    if answer.lower() == str(result).lower():
        print("Correct!")
        attempt += 1
        if attempt == limit:
            print(f"Congratulations, {name}!")
            return attempt, True
        else:
            return attempt, False
    else:
        print(f'''\'{answer}\' is wrong answer ;(. \
Correct answer was \'{result}\'
Let\'s try again, {name}''')
        attempt = 0
        return attempt, True


def main():
    name = cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    attempt = 0
    end = False
    while not end:
        result = even()
        answer = prompt.string('Your answer: ')
        attempt, end = respondent(name, answer, result, attempt)


if __name__ == "__main__":
    main()
