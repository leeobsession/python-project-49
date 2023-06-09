#!/usr/bin/env python3
from brain_games.cli import welcom_user
import random
import prompt
import math

print('Welcome to the Brain Games! ')
name = prompt.string('May I have your name? ')
welcom_user(name)
text = 'is wrong answer ;(. Correct answer was'


def logic_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    win = 0
    while win < 3:
        i = random.randint(1, 100)
        print(f'Question: {i}')
        answer = prompt.string("Your answer: ")
        if (i % 2 == 0 and answer == 'yes') or (i % 2 != 0 and answer == 'no'):
            print('Correct!')
        elif i % 2 == 0 and answer != 'yes':
            return print(f'''"{answer}" {text} "yes".
Let\'s try again, {name}!''')
            break
        elif i % 2 != 0 and answer != 'no':
            return print(f'''"{answer}" {text} "no".
Let\'s try again, {name}!''')
            break
        win = win + 1
    else:
        return print(f'Congratulations, {name}!')


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


def is_prime(a):
    if a < 2:
        return False
    for i in range(2, int(a ** 0.5 + 1)):
        if a % i == 0:
            return False
    else:
        return True


def logic_prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    win = 0

    while win < 3:
        i = random.randint(1, 30)
        print(f'Question: {i}')
        prime = is_prime(i)
        answer = prompt.string("Your answer: ")
        if prime is True and answer == 'yes':
            print('Correct!')
        elif prime is False and answer == 'no':
            print('Correct!')
        elif prime is True and answer != 'yes':
            return print(f'''"{answer}" {text} "yes".
Let's try again, {name}!''')
            break
        elif prime is False and answer != 'no':
            return print(f'''"{answer}" {text} "no".
Let's try again, {name}!''')
            break
        win = win + 1
    else:
        return print(f'Congratulations, {name}!')


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


def logic_progression():
    print('What number is missing in the progression?')
    win = 0
    while win < 3:
        x = random.randint(10, 20)
        y = random.randint(50, 60)
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

# end
