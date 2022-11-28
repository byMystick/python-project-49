import random
import operator
game_name = 'What is the result of the expression?'
operators = ["+", "-", "*"]


def create_question_answer():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    operator_ = random.choice(operators)
    question = f"{number_1} {operator_} {number_2}"
    if operator_ == "+":
        result = operator.add(number_1, number_2)
    elif operator_ == "-":
        result = operator.sub(number_1, number_2)
    else:
        result = operator.mul(number_1, number_2)
    return question, result
