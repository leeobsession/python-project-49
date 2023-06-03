#!/usr/bin/env python3
import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    win = 0

    while win < 3:
        i = random.randint(1, 100)
        print(f'Question: {i}')
        answer = prompt.string("Your answer: ")

        if (i % 2 == 0 and answer == 'yes') or (i % 2 != 0 and answer == 'no'):
            print('Correct!')
        elif i % 2 == 0 and answer != 'yes':
            print(f'"{answer}" is wrong answer ;(. Correct answer was "yes".')
            print(f'Let\'s try again, {name}!')
            break
        elif i % 2 != 0 and answer != 'no':
            print(f'"{answer}" is wrong answer ;(. Correct answer was "no".')
            print(f'Let\'s try again, {name}!')
            break
        win = win + 1
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':

    main()

# end main
