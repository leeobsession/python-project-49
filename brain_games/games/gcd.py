from random import randint
from math import gcd


TASK_GAME = 'Find the greatest common divisor of given numbers.'
NUM_MIN = 1
NUM_MAX = 30


def start_game():
    num_one = randint(NUM_MIN, NUM_MAX)
    num_two = randint(NUM_MIN, NUM_MAX)
    a = num_one
    b = num_two
    question = f'{num_one} {num_two}'
    true_answer = gcd(a, b)
    return question, str(true_answer)
