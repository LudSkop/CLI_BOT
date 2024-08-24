expenses = {
    "hotel": 150,
    "breakfast": 30,
    "taxi": 15,
    "lunch": 20
}


file_name = "expenses.txt"
with open(file_name, "w") as fh:
    for key, value in expenses.items():
        fh.write(f"{key}|{value}\n")