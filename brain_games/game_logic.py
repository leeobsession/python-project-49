import prompt


TEXT = 'is wrong answer ;(. Correct answer was'
WIN = 3


def logic_games(game):
    print('Welcome to the Brain Games! ')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    count_round = 0

    print(game.TASK_GAME)
    while count_round < WIN:
        count_round += 1
        question, true_answer = game.start_game()
        print(f'Question: {question}')
        user_answer = prompt.string("Your answer: ")
        if user_answer == true_answer:
            print('Correct!')
        else:
            print(f'''"{user_answer}" {TEXT} "{true_answer}".
Let's try again, {name}!''')

            return
    print(f'Congratulations, {name}!')
