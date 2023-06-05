#!/usr/bin/env python3
import random
import prompt


def brain_progression():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    text = 'is wrong answer ;(. Correct answer was'
    win = 0
    while win < 3:
        x = random.randint(10, 20)
        y = random.randint(50, 60)
        z = random.randint(5, 10)
        pro_list = list(range(x, y, z))
        answer = random.choice(pro_list)
        pro_string = ' '.join(str(n) for n in pro_list)
        answer_secret = pro_string.replace(str(answer), '..', 1)
        print(f'Question: {answer_secret}')
        user_answer = prompt.integer('Your answer: ')
        if answer == user_answer:
            print('Correct!')
        elif answer != user_answer:
            print(f'"{user_answer}" {text} "{answer}".')
            print(f"Let's try again, {name}!")
            break
        win += 1
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':

    brain_progression()

# end
