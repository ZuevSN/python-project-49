import prompt
import random


def equality(num, answer):
    if num % 2 == 0:
        result_num = 'yes'
    else:
        result_num = 'no'
    if answer.lower() == result_num:
        return True, result_num
    else:
        return False, result_num


def main(name='anonymous', end=3):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for step in range(0, end):
        random_number = random.randint(1, 100)
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        equal, result_num = equality(random_number, answer)
        if equal:
            print("Correct!")
            if step == 2:
                print(f"Congratulations, {name}!")
        else:
            print(f'''\'{answer}\' is wrong answer ;(. \
Correct answer was \'{result_num}\'
Let\'s try again, {name}''')

            break


if __name__ == "__main__":
    main()
