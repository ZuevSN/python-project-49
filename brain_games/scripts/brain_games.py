#!/usr/bin/env python3
from brain_games.scripts import cli
from brain_games.scripts import brain_even


def main():
    print("Welcome to the Brain Games!")
    name = cli.welcome_user()
    brain_even.main(name)


if __name__ == "__main__":
    main()
