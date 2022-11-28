from random import randint
game_name = 'Answer "yes" if the number is even, otherwise answer "no".'


def create_question_answer():
    number = randint(1, 100)
    answer = 'yes' if number % 2 == 0 else 'no'
    return number, answer
