import random
import prompt


print('Welcome to the Brain Games! ')
name = prompt.string('May I have your name? ')
print(f"Hello, {name}!")
text = 'is wrong answer ;(. Correct answer was'


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
