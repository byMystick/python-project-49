# In this code we are not using librory 'math'. We bild a funkcion.
import random
import prompt
from brain_games.cli import welcome_user


# Euclid's algorithm
def gcd_by_euclid(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def gcd():
    name = welcome_user()   # import greeting
    print('Find the greatest common divisor of given numbers.')
    score = 1   # keep score
    while score <= 3:   # cycle up to 3
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        print(f'Question: {number1} {number2}')
        answer_user = prompt.string('Your answer: ')
        # function 'gcd_by_euclid' result to variable
        answer = gcd_by_euclid(number1, number2)
        if str(answer_user) == str(answer):
            score += 1
            print('Correct!')
        else:
            print(f"'{answer_user}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'."
                  f"\nLet's try again, {name}!")
            break
    if score > 3:
        print(f'Congratulations, {name}')
