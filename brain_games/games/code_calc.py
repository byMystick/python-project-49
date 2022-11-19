import random
game_post = 'What is the result of the expression?'


def game():
    # generate number 1
    x = random.randint(1, 100)
    # generate number 2
    y = random.randint(1, 100)
    operators = ['-', '+', '*']
    make_choice = random.choice(operators)
    operation = {'-': (x - y), '+': (x + y), '*': (x * y)}
    question = (str(x) + ' ' + make_choice + ' ' + str(y))
    result = str(operation[make_choice])
    return question, result
