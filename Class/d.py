import csv


FILENAME = 'users.csv'

users = [
    {'name': 'Oleg', 'age': '51', 'sex': 'male', 'animal': 'False'},
    {'name': 'Vlad', 'age': '24', 'sex': 'male', 'animal': 'False'},
    {'name': 'luda', 'age': '43', 'sex': 'female','animal': 'False'},
    {'name': 'Alice', 'age': '7', 'sex': 'female','animal': 'False'},
    {'name': 'Pusa', 'age': '4', 'sex': 'female','animal': 'False'},

]

with open(FILENAME, mode='w', newline='', encoding='utf-8') as file:
    columns = ['name', 'age', 'sex']
    writer = csv.DictWriter(file, delimiter=',', fieldnames=columns)
    writer.writeheader()
    for ron in users:
        writer.writerow(ron)