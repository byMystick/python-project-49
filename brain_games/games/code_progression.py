import random
game_name = 'What number is missing in the progression?'


def create_a_progression_and_length():
    start_of_progression = random.randint(1, 100)
    step = random.randint(1, 10)
    progression_length = random.randint(5, 10)
    end_of_progression = start_of_progression + step * progression_length
    progression = list(range(start_of_progression, end_of_progression, step))
    return progression, progression_length


def create_question_answer():
    progression, progression_length = create_a_progression_and_length()
    random_number = (random.randint(0, progression_length - 1))
    answer = progression[random_number]
    progression[random_number] = '..'
    question = ''
    for number in progression:
        question += f'{number} '
    question = question.strip()
    return question, answer
