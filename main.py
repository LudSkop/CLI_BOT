from collections import UserList
import re
from colorama import Fore
from datetime import datetime


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if value.isdigit() and len(value) == 10:
            super().__init__(value)
        else:
            raise ValueError("Invalid phone number format.")


class Email(Field):
    def __init__(self, value):
        self.value = value
        pattern = r"^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$"
        if re.match(pattern, value):
            super().__init__(value)
        else:
            raise ValueError("Invalid email")


class Birthday(Field):
    def __init__(self, value):
        self.value = value
        date_format = "%Y-%m-%d"
        parsed_date = datetime.strptime(value, date_format).date()
        if parsed_date > datetime.now().date():
            raise ValueError(
                Fore.LIGHTRED_EX + "Birthday date cannot be in the future"
            )
        super().__init__(value)



class Record:

    def __init__(self, name, phone, email, birthday):
        self.name = Name(name)
        self.phones = []
        self.phones.append(Phone(phone))
        self.email = Email(email)
        self.birthday = Birthday(birthday)

    def __str__(self):
        return f"{Fore.MAGENTA}Name: {self.name}\n{Fore.RED}Phone: {[phone.value for phone in self.phones]}\n{Fore.CYAN}Email: {self.email}\n{Fore.YELLOW}Birthday: {self.birthday}{Fore.RESET}"

    def add_phone(self, number_phone):
        new_phone = Phone(number_phone)
        self.phones.append(new_phone)

    def remove_phone(self, phone_v):
        for phone in self.phones:
            if phone.value == phone_v:
                self.phones.remove(phone)

    def edit_phone(self, new_phone, old_phone):
        for el in self.phones:
            if el.value == old_phone:
                self.phones.remove(el)
                new_phone = Phone(new_phone)
                self.phones.append(new_phone)


    def find_phone(self, phone):
        for el in self.phones:
            if el.value == phone:
                return el



class AddressBook(UserList):
    def add_record(self, record):
        self.append(record)

    def find_record(self, name):
        for record in self:
            if record.name == name:
                return record
        return None

    def remove_record(self, name):
        record = self.find_record(name)
        if record:
            self.remove(record)
        else:
            print(Fore.LIGHTRED_EX + "Record not found.")

    def update_record(self, name, phone=None, email=None, birthday=None):
        record = self.find_record(name)
        if record:
            if phone:
                record.phone = Phone(phone)
            if email:
                record.email = Email(email)
            if birthday:
                record.birthday = Birthday(birthday)
        else:
            print(Fore.LIGHTRED_EX + "Record not found.")


if __name__ == '__main__':
    record_vlad = Record('Vlad', '0963610573', 'qwe@gmail.com', '2000-01-28')
    record_vlad.remove_phone('0963610573')
    record_vlad.add_phone('0963234404')
    record_vlad.edit_phone('1234567890','0963234404')
    record_vlad.add_phone("1231231231")
    record_vlad.add_phone('9876543210')
    record_vlad.remove_phone('1231231231')
    print(record_vlad.find_phone('1234567890'))
    print(record_vlad)











