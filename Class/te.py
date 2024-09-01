import csv


name = 'table.csv'
with open(name, mode='w') as file:
    writer = csv.writer(file)
    for item in range(1, 100):
        writer.writerow([item, item ** 2, item ** 3])

with open(name, mode='r') as file:
    reader = csv.reader(file)
    res = []
    for line in reader:
        res.append(line)
    print(res)

