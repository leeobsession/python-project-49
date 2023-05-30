import prompt


def welcom_user():

    name = prompt.string('May I have your name?')

    return f"Hello, {name}!"
