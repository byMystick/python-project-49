from random import randint
import prompt
from brain_games.cli import welcome_user


def parity_check():
    name = welcome_user()   # import greeting
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct = 1     # keep score
    while correct <= 3:     # cycle up to 3
        number = randint(1, 100)
        print(f'Question: {number}')    # give a number
        answer_user = prompt.string('Your answer: ')    # we get an answer
        answer = ''
        # checking the answer
        if number % 2 == 0:
            answer += 'yes'
        if number % 2 != 0:
            answer += 'no'
        if str(answer_user) == str(answer):
            print('Correct!')
            correct += 1
        else:
            print(f"'{answer_user}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'."
                  f"\nLet's try again, {name}!")
            break
    if correct > 3:
        return print(f'Congratulations, {name}!')
