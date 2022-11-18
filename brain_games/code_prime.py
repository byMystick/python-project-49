import random
import prompt
from brain_games.cli import welcome_user


# check if the number is prime or not
def number(random_number):
    if random_number < 2:
        return False
    for i in range(2, random_number):
        if random_number % i == 0:
            return False
    return True


# form a question and answer
def question_answer():
    question = random.randint(1, 100)
    answer = number(question) and 'yes' or 'no'
    print(f'Question: {question}')
    return str(question), str(answer)


def prime():
    name = welcome_user()  # import greeting
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    score = 1  # keep score
    while score <= 3:  # cycle up to 3
        # function 'answer' result to variable
        question, answer = question_answer()
        answer_user = prompt.string("Your answer: ")
        if str(answer) == str(answer_user):
            print('Correct!')
            score += 1
        else:
            print(f"'{answer_user}' is wrong answer ;(."
                  f"Correct answer was '{answer}'."
                  f"\nLet's try again, {name}!")
            break
    if score > 3:
        return print(f'Congratulations, {name}!')
