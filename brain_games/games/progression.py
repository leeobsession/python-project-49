from brain_games.cli import welcome_user
import random
import prompt


print('Welcome to the Brain Games! ')
NAME = prompt.string('May I have your name? ')
welcom_user(name)
TEXT = 'is wrong answer ;(. Correct answer was'


def logic_progression():
    print('What number is missing in the progression?')
    win = 0
    while win < 3:
        x = random.randint(4, 15)
        y = random.randint(57, 63)
        z = random.randint(3, 8)
        pro_list = list(range(x, y, z))
        answer = random.choice(pro_list)
        pro_string = ' '.join(str(n) for n in pro_list)
        answer_secret = pro_string.replace(str(answer), '..', 1)
        print(f'Question: {answer_secret}')
        user_answer = prompt.integer('Your answer: ')
        if answer == user_answer:
            print('Correct!')
        elif answer != user_answer:
            return print(f'''"{user_answer}" {text} "{answer}".
Let's try again, {name}!''')
            break
        win += 1
    else:
        return print(f'Congratulations, {name}!')
