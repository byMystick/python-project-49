import random
import prompt
from brain_games.cli import welcome_user


def answer():   # determine the answer
    numbers_1 = random.randint(1, 99)
    numbers_2 = random.randint(1, 99)
    operator = random.choice(['-', '+', '*'])
    print(f'{numbers_1} {operator} {numbers_2}')
    answer_b = ''
    if operator == '-':
        answer_b = numbers_1 - numbers_2
    elif operator == '+':
        answer_b = numbers_1 + numbers_2
    elif operator == '*':
        answer_b = numbers_1 * numbers_2
    return answer_b


def calc():
    name = welcome_user()   # import greeting
    print('What is the result of the expression?')
    score = 1   # keep score
    while score <= 3:   # cycle up to 3
        x = answer()    # function 'answer' result to variable
        answer_user = prompt.string("Your answer: ")
        if str(x) == str(answer_user):
            print('Correct!')
            score += 1
        else:
            print(f'{answer_user} is wrong answer ;(. Correct answer was {x}.')
            break
    if score > 3:
        return print(f'Congratulations, {name}!')
