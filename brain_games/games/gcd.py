import random
import prompt
import math


print('Welcome to the Brain Games! ')
name = prompt.string('May I have your name? ')
print(f"Hello, {name}!")
text = 'is wrong answer ;(. Correct answer was'


def logic_gcd():
    print('Find the greatest common divisor of given numbers.')
    win = 0
    while win < 3:
        x = random.randint(1, 50)
        y = random.randint(1, 50)

        a = x
        b = y
        random_quest = f'{x} {y}'
        print(f'Question: {random_quest}')
        user_answer = prompt.integer('Your answer: ')
        nod = math.gcd(a, b)
        if nod == user_answer:
            print('Correct!')
        elif nod != user_answer:
            return print(f'''"{user_answer}" {text} "{nod}".
Let's try again, {name}!''')
            break
        win += 1
    else:
        return print(f'Congratulations, {name}!')
