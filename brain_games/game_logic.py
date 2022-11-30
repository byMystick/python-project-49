from brain_games.cli import welcome_user
import prompt
final_score = 3


def run_game(module):
    game_score = 0
    name = welcome_user()
    print(module.game_name)
    for game_score in range(final_score):
        question, answer = module.create_question_answer()
        print(f'Question: {question}')
        answer_user = prompt.string('Your answer: ')
        if str(answer_user) == str(answer):
            print('Correct!')
            game_score += 1
        else:
            print(f"'{answer_user}' is wrong answer ;(."
                  f" Correct answer was '{answer}'."
                  f"\nLet's try again, {name}!")
            break
    if game_score == final_score:
        print(f'Congratulations, {name}!')
