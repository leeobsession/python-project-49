from brain_games import cli
import random
import prompt


print('Welcome to the Brain Games! ')
NAME = prompt.string('May I have your name? ')
welcom_user(name)
TEXT = 'is wrong answer ;(. Correct answer was'

def logic_calc():

    print('What is the result of the expression?')
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    v = random.randint(1, 100)
    c = random.randint(1, 80)
    n = random.randint(1, 30)
    p = random.randint(1, 30)
    operand_list = (f"{x} + {y}", f"{v} - {c}", f"{n} * {p}")
    win = 0
    while win < 3:
        random_quest = random.choice(operand_list)
        answer = eval(random_quest)
        print(f'Question: {random_quest}')
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
