import random
import operator
game_name = 'What is the result of the expression?'


def generate_responses():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    result = random.choice([operator.add(number_1, number_2),
                            operator.mul(number_1, number_2),
                            operator.sub(number_1, number_2)])
    question = ''
    if result == operator.add(number_1, number_2):
        question = f'{number_1} + {number_2}'
    elif result == operator.mul(number_1, number_2):
        question = f'{number_1} * {number_2}'
    elif result == operator.sub(number_1, number_2):
        question = f'{number_1} - {number_2}'
    return question, result
