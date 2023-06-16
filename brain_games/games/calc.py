from random import randint, choice


TASK_GAME = 'What is the result of the expression?'
NUM_MIN = 1
NUM_MAX = 30
OPERATORS = ['+', '-', '*']


def calculate_expression(num_one, num_two, operator):
    if operator == '+':
        correct_answer = num_one + num_two
    elif operator == '-':
        correct_answer = num_one - num_two
    elif operator == '*':
        correct_answer = num_one * num_two
    return correct_answer


def start_game():
    one_num = randint(NUM_MIN, NUM_MAX)
    two_num = randint(NUM_MIN, NUM_MAX)
    operator = choice(OPERATORS)
    question = f'{one_num} {operator} {two_num}'
    correct_answer = calculate_expression(one_num, two_num, operator)
    return question, str(correct_answer)
