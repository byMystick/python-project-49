from random import randint
import prompt


def parity_check():
    print('Welcome to the Parity check Game!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct = 1     # keep score
    while correct <= 3:     # cycle up to 3
        number = randint(1, 100)
        print(f'Question: {number}')    # give a number
        answer = prompt.string('Your answer: ')     # we get an answer
        # checking the answer
        if number % 2 == 0 and answer == str('yes') \
                or number % 2 != 0 and answer == str('no'):
            print('Correct!')
            correct += 1
        elif number % 2 == 0 and answer == str('no'):
            print(f"'no' is wrong answer ;(. Correct answer was 'yes'. "
                  f"Let's try again, {name}!")
            break
        elif number % 2 != 0 and answer == str('yes'):
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'."
                  f"Let's try again, {name}!")
            break
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was 'yes/no'."
                  f"Let's try again, {name}!")
            break
    if correct > 3:
        return print(f'Congratulations, {name}!')
