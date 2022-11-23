import random
game_name = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# check if the number is prime or not
def generate_number(random_number):
    if random_number < 2:
        return False
    for i in range(2, random_number):
        if random_number % i == 0:
            return False
    return True


# form a question and answer
def generate_responses():
    question = random.randint(1, 100)
    answer = 'yes' if generate_number(question) else 'no'
    return question, answer
