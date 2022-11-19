import random
game_post = 'What number is missing in the progression?'


def game():
    start_progression = random.randint(1, 100)  # generate start number
    step = random.randint(1, 10)    # generate step
    # generate progression length
    progression_length = random.randint(5, 10)
    # determine the end of the progression
    end_progression = start_progression + step * progression_length
    # make a progression
    progression = (list(range(start_progression, end_progression, step)))
    # determine the number for the question
    random_number = (random.randint(0, progression_length - 1))
    answer = progression[random_number]
    # replace the number in progression with '..'
    progression[random_number] = '..'
    question = ''
    for number in progression:
        question = question + str(number) + " "
    question = question.strip()
    return str(question), str(answer)
