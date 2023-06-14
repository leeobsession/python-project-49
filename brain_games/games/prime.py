from random import randint


TASK_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'
NUM_MIN = 1
NUM_MAX = 30


def is_prime(a):
    if a < 2:
        return 'no'
    for i in range(2, int(a ** 0.5 + 1)):
        if a % i == 0:
            return 'no'
    else:
        return 'yes'


def start_game():
    num = randint(NUM_MIN, NUM_MAX)
    question = num
    true_answer = is_prime(question)
    return str(question), true_answer
