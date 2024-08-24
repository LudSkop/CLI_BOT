file_name = "expenses.txt"
expenses = {}
with open(file_name, "r") as fh:
    raw_expenses = fh.readlines()
    for line in raw_expenses:
        key, value = line.split("|")
        expenses[key] = int(value)