from random import randint
game_name = 'Answer "yes" if the number is even, otherwise answer "no".'


def game():
    number = randint(1, 100)
    answer = ''
    if number % 2 == 0:
        answer += 'yes'
    if number % 2 != 0:
        answer += 'no'
    return number, answer
