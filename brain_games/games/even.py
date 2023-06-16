from random import randint


TASK_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'
NUM_MIN = 1
NUM_MAX = 100


def is_even(num):
    if num % 2 == 0:
        return True


def start_game():
    num = randint(NUM_MIN, NUM_MAX)
    question = num
    correct_answer = 'yes' if is_even(num) else 'no'
    return str(question), correct_answer
