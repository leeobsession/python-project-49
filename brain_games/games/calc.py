from random import randint, choice


TASK_GAME = 'What is the result of the expression?'
NUM_MIN = 1
NUM_MAX = 30
OPERATORS = ['+', '-', '*']


def start_game():
    one_num = randint(NUM_MIN, NUM_MAX)
    two_num = randint(NUM_MIN, NUM_MAX)
    operator = choice(OPERATORS)
    question = f'{one_num} {operator} {two_num}'
    true_answer = eval(question)
    return question, str(true_answer)
