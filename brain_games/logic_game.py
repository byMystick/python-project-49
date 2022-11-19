from brain_games.cli import welcome_user
import prompt


def run_game(module):
    name = welcome_user()
    print(module.game_post)
    score = 0
    while 0 <= score < 3:
        question, answer = module.game()
        print(f'Question: {question}')
        answer_user = prompt.string('Your answer: ')
        if str(answer_user) == str(answer):
            score += 1
            print('Correct!')
        else:
            print(f"'{answer_user}' is wrong answer ;(. "
                  f" Correct answer was '{answer}'."
                  f"\nLet's try again, {name}!")
            break
    if score == 3:
        print(f'Congratulations, {name}!')
