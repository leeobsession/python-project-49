from random import randint
from math import gcd


TASK_GAME = 'Find the greatest common divisor of given numbers.'
NUM_MIN = 1
NUM_MAX = 30


def start_game():
    num_one = randint(NUM_MIN, NUM_MAX)
    num_two = randint(NUM_MIN, NUM_MAX)
    question = f'{num_one} {num_two}'
    correct_answer = gcd(question)
    return question, str(correct_answer)
