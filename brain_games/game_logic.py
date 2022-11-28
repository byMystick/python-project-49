from brain_games.cli import welcome_user
import prompt


def run_game(module):
    game_score = 0
    name = welcome_user()
    print(module.game_name)
    for game_score in range(3):
        question, answer = module.create_question_answer()
        print(f'Question: {question}')
        answer_user = prompt.string('Your answer: ')
        if str(answer_user) == str(answer):
            print('Correct!')
            game_score += 1
        else:
            print(f"'{answer_user}' is wrong answer ;(. "
                  f" Correct answer was '{answer}'."
                  f"\nLet's try again, {name}!")
            break
    if game_score == 3:
        print(f'Congratulations, {name}!')
