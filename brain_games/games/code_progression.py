import random
game_name = 'What number is missing in the progression?'


def generate_responses():
    start_of_progression = random.randint(1, 100)  # generate start number
    step = random.randint(1, 10)    # generate step
    # generate progression length
    progression_length = random.randint(5, 10)
    # determine the end of the progression
    end_of_progression = start_of_progression + step * progression_length
    # make a progression
    progression = list(range(start_of_progression, end_of_progression, step))
    # determine the number for the question
    random_number = (random.randint(0, progression_length - 1))
    answer = progression[random_number]
    # replace the number in progression with '..'
    progression[random_number] = '..'
    question = ''
    for number in progression:
        question += f'{number} '
    question = question.strip()
    return question, answer
