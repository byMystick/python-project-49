# In this code we are not using librory 'math'. We bild a funkcion.
import random
game_post = 'Find the greatest common divisor of given numbers.'


# Euclid's algorithm
def gcd_by_euclid(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def game():
    number1 = random.randint(1, 100)    # create a number1
    number2 = random.randint(1, 100)    # create a number2
    # get an answer
    answer = gcd_by_euclid(number1, number2)
    # get an question
    question = f'{number1} {number2}'
    return question, answer
