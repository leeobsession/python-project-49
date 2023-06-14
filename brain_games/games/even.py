from random import randint


TASK_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'
NUM_MIN = 1
NUM_MAX = 100


def even_num(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def start_game():
    num = randint(NUM_MIN, NUM_MAX)
    question = num
    true_answer = even_num(num)
    return str(question), true_answer
