import random
game_name = "What number is missing in the progression?"


def make_progression():
    start_progression = random.randint(1, 100)
    step_progression = random.randint(2, 12)
    progression_length = random.randint(5, 10)
    progression = [start_progression]
    for i in range(progression_length):
        progression.append(progression[i] + step_progression)
    return progression


def create_question_answer():
    progression = make_progression()
    answer = random.choice(progression)
    number_index = progression.index(answer)
    progression[number_index] = '..'
    question = (' '.join(map(str, progression)))
    return question, answer
