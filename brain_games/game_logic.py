from brain_games.cli import welcome_user
import prompt


def run_game(module):
    final_score = 3
    name = welcome_user()
    print(module.game_name)
    for i in range(final_score):
        question, answer = module.generate_responses()
        print(f'Question: {question}')
        answer_user = prompt.string('Your answer: ')
        if str(answer_user) == str(answer):
            print('Correct!')
            i += 1
        else:
            print(f"'{answer_user}' is wrong answer ;(. "
                  f" Correct answer was '{answer}'."
                  f"\nLet's try again, {name}!")
            break
    if i == 3:
        print(f'Congratulations, {name}!')
