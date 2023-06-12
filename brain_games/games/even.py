from brain_games.cli import welcome_user
import random
import prompt


print('Welcome to the Brain Games! ')
NAME = prompt.string('May I have your name? ')
welcom_user(name)
TEXT = 'is wrong answer ;(. Correct answer was'


def logic_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    win = 0
    while win < 3:
        i = random.randint(1, 100)
        print(f'Question: {i}')
        answer = prompt.string("Your answer: ")
        if i % 2 == 0 and answer == 'yes':
            print('Correct!')
        elif i % 2 != 0 and answer == 'no':
            print('Correct!')
        elif i % 2 == 0 and answer != 'yes':
            return print(f'''"{answer}" {text} "yes".
Let's try again, {name}!''')
            break
        elif i % 2 != 0 and answer != 'no':
            return print(f'''"{answer}" {text} "no".
Let's try again, {name}!''')
            break
        win = win + 1
    else:
        return print(f'Congratulations, {name}!')
