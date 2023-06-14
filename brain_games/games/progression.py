from random import randint, choice


TASK_GAME = 'What number is missing in the progression?'


def start_game():
    start_num = randint(4, 15)
    stop_num = randint(57, 63)
    step_num = randint(3, 8)
    pro_list = list(range(start_num, stop_num, step_num))
    pro_string = ' '.join(str(n) for n in pro_list)
    true_answer = choice(pro_list)
    question = pro_string.replace(str(true_answer), '..', 1)
    return question, str(true_answer)
