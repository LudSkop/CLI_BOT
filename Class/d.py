import csv


FILENAME = 'users.csv'

users = [
    {'name': 'Oleg', 'age': '51', 'sex': 'male', 'animal': 'False'},
    {'name': 'Vlad', 'age': '24', 'sex': 'male', 'animal': 'False'},
    {'name': 'Luda', 'age': '43', 'sex': 'female','animal': 'False'},
    {'name': 'Alice', 'age': '7', 'sex': 'female','animal': 'True'},
    {'name': 'Pusa', 'age': '4', 'sex': 'female','animal': 'True'},

]

with open(FILENAME, mode='w', newline='', encoding='utf-8') as file:
    columns = ['name', 'age', 'test','sex','animal', 'data', 'mont']
    writer = csv.DictWriter(file, delimiter=',', fieldnames=columns)
    writer.writeheader()
    for ron in users:
        writer.writerow(ron)

with open(FILENAME, mode='r', newline='', encoding='utf-8')as file:
    reader = csv.DictReader(file)
    for ron in reader:
        #print(ron)
        print(ron['name'])
        print(ron.get('age'))