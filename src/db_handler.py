def database_shit(list):
    user_id = list[0]
    username = list[1]
    with open('users.txt', mode='a') as f:
        f.write(f'[{user_id}, {username}] \n')
        f.close()
