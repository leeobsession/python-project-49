#!/usr/bin/env python3
import random
import prompt
import math


def brain_gcd():
    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')

    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    text = 'is wrong answer ;(. Correct answer was'
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
            print(f'"{user_answer}" {text} "{nod}".')
            print(f"Let's try again, {name}!")
            break
        win += 1
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':

    brain_gcd()

# end
