import random
from colorama import Fore


def get_participants():
    with open('users.txt') as f:
        lines = [line for line in f]

    with open('users.txt') as f:
        lines = [line.rstrip() for line in f]

    arr = []

    for line in lines:
        arr.append(line)

    return arr


def decide_winner(arr):
    winner = random.choice(arr)
    print(Fore.RED + f'THE WINNER IS: {winner}')


def main():
    decide_winner(get_participants())


if __name__ == '__main__':
    main()
