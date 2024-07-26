import re
from typing import Callable

t = ("Загальний дохід працівника складається з декількох частин:\n"
     "1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів.")


def generator_numbers(text: str):
    numbers = re.findall(r'\b-?\d+\.\d+\b', text)
    for el in numbers:
        yield float(el)


def sum_profit(text: str, func: Callable):
    numbers = func(text)
    total = sum(numbers)
    return total


res = generator_numbers(t)
res_sum = sum_profit(t, generator_numbers)

print(res)
print(res_sum)
from tabulate import tabulate


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, KeyError, IndexError):
            return 'Give me name and phone please'
        except Exception as e:
            return f"An unexpected error occurred: {e}"
    return inner


headers = ["ім'я", "телефон"]


@input_error
def parse_input(user_input: str) -> tuple:
    cmd, *args = user_input.split()
    cmd = cmd.lower()
    return cmd, *args


@input_error
def add_contact(args: tuple, contacts: dict) -> str:
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return 'Контакт оновлено'
    else:
        contacts[name] = phone
        return 'Контакт додано'


@input_error
def show_all_contacts(contacts: dict) -> str:
    contacts = [[name, phone] for name, phone in contacts.items()]
    table = tabulate(contacts, headers=headers, tablefmt="grid")
    return table


@input_error
def show_contact(args: tuple, contacts: dict) -> str:
    name = args[0]
    phone = contacts.get(name, "Контакт не знайдено")
    contact = [[name, phone]]
    table = tabulate(contact, headers=headers, tablefmt='grid')
    return table


@input_error
def main():
    contacts = {}
    print("Ласкаво просимо в асистент бота!!!>>>")

    while True:
        user_input = input("Введіть вашу команду : >>> ").strip().lower()
        command, *args = parse_input(user_input)
        if command in ["exit", "close"]:
            print("До побачення!!!")
            break
        elif command == 'hello':
            print("Привіт чим можу допомогти?")
        elif command in ["add", "change"]:
            print(add_contact(args, contacts))
        elif command == 'all':
            print(show_all_contacts(contacts))
        elif command == 'show_phone':
            print(show_contact(args, contacts))

        else:
            print("Ви ввели некоректну команду!!!")


if __name__ == "__main__":
    main()