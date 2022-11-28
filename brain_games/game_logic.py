from brain_games.cli import welcome_user
import prompt
score = 0

def run_game(module):
    name = welcome_user()
    print(module.game_name)
    for score in range(3):
        question, answer = module.generate_responses()
        print(f'Question: {question}')
        answer_user = prompt.string('Your answer: ')
        if str(answer_user) == str(answer):
            print('Correct!')
            score += 1
        else:
            print(f"'{answer_user}' is wrong answer ;(. "
                  f" Correct answer was '{answer}'."
                  f"\nLet's try again, {name}!")
            break
    if score == 3:
        print(f'Congratulations, {name}!')
