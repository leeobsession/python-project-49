#!/usr/bin/env python3
import random
import prompt


def main():
    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')

    print(f'Hello, {name}!')
    
    print('What is the result of the expression?')
    text = 'is wrong answer ;(. Correct answer was'
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    operand_list = (f"{x} + {y}", f"{x} - {y}", f"{x} * {y}")
    win = 0
    while win < 3:
        random_quest = random.choice(operand_list)
        answer = eval(random_quest)
        print(f'Question: {random_quest}')
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

    main()

# end
