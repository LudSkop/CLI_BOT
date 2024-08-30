import pickle

FILENAME ='user.dat'
users = [
    ['Alice', 8, True],
    ['Oleg', 52, False],
    ['Vlad', 24, True],
]

with open(FILENAME,'wb' ) as file:
    pickle.dump(users, file)

with open(FILENAME, 'rb') as file_1:
    users_from_file = pickle.load(file_1)
    for user in users_from_file:
        print('Name: ', user[0], '\tAge:', user[1])