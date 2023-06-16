from random import randint, choice


TASK_GAME = 'What number is missing in the progression?'
LENGTH = 6


def generate_expression(start, stop, step):
    progression_list = list(range(start, stop, step))
    return progression_list[LENGTH:]


def start_game():
    start_num = randint(4, 15)
    stop_num = randint(57, 63)
    step_num = randint(3, 8)
    progression = generate_expression(start_num, stop_num, step_num)
    pro_string = ' '.join(str(n) for n in progression)
    correct_answer = choice(pro_string)
    question = pro_string.replace(str(correct_answer), '..', 1)
    return question, str(correct_answer)
