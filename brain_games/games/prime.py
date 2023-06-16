from random import randint


TASK_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'
NUM_MIN = 1
NUM_MAX = 30


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5 + 1)):
        if num % i == 0:
            return False
    else:
        return True


def start_game():
    num = randint(NUM_MIN, NUM_MAX)
    question = num
    correct_answer = 'yes' if is_prime(question) else 'no'
    return str(question), correct_answer
