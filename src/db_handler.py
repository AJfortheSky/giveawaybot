import random

def database_shit(list):
    user_id = list[0]
    username = list[1]
    with open('users.txt', mode='a') as f:
        f.write(f'[{user_id}, {username}] \n')
        f.close()



def get_winner():
    with open('users.txt') as f:
        lines = [line for line in f]


    # removing the new line characters
    with open('users.txt') as f:
        lines = [line.rstrip() for line in f]


    arr = []

    for line in lines:
        arr.append(line)

    return arr


def decide_winner(arr):
    winner = random.choice(arr)
    print(winner)


decide_winner(get_winner())