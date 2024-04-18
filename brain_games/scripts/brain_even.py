import prompt
import random
from brain_games.scripts import cli


def even():
    random_number = random.randint(1, 100)
    print(f'Question: {random_number}')
    if random_number % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return result


# функция принимает ответ, верный результат, число успехов и
# ограничитель правильных ответов.
# При обработке: выдает сообщения при успехах и неуспехах;
# возвращает номер попытки и закончена игра или нет.
def respondent(name: str, answer: str, result, score: int, limit=3):
    if answer.lower() == str(result).lower():
        print("Correct!")
        score += 1
        if score == limit:
            print(f"Congratulations, {name}!")
            end = True
            return score, end
        else:
            end = False
            return score, end
    else:
        print(f'''\'{answer}\' is wrong answer ;(. \
Correct answer was \'{result}\'
Let\'s try again, {name}''')
        score = 0
        end = True
        return score, end


def main():
    name = cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    score = 0
    end = False
    while not end:
        result = even()
        answer = prompt.string('Your answer: ')
        score, end = respondent(name, answer, result, score)


if __name__ == "__main__":
    main()
