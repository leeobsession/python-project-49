#!/usr/bin/env python3
from brain_games.cli import welcom_user
import prompt


def main():
    print('Welcome to the Brain Games! ')
    name = prompt.string('May I have your name?')
    welcom_user(name)


if __name__ == "__main__":

    main()

# end main
