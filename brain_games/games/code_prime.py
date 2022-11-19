import random
game_post = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# check if the number is prime or not
def number(random_number):
    if random_number < 2:
        return False
    for i in range(2, random_number):
        if random_number % i == 0:
            return False
    return True


# form a question and answer
def game():
    question = random.randint(1, 100)
    answer = number(question) and 'yes' or 'no'
    return str(question), str(answer)
