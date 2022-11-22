import random
game_name = 'What is the result of the expression?'


def generate_responses():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    operator = random.choice(['-', '+', '*'])
    if operator == '-':
        result = number_1 - number_2
    elif operator == '+':
        result = number_1 + number_2
    elif operator == '*':
        result = number_1 * number_2
    question = f'{number_1} {operator} {number_2}'
    return question, result
