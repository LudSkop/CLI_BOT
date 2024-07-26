from collections import UserList

from table import table_decorator


class Contact:
    __headers = ["Name", "Phone", "Address"]

    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address

    def edit_contact(self):
        new_name = input("Enter new name")
        new_phone = input("Enter new phone")
        new_address = input("Enter new address")
        self.name = new_name if new_name else self.name
        self.phone = new_phone if new_phone else self.phone
        self.address = new_address if new_address else self.address
        return "Contact edit successesfully"

    @table_decorator(__headers)
    def __str__(self):

        return [
            [
                self.name,
                self.phone,
                self.address,
            ]
        ]


class AddressBook(UserList):

    def add_contact(self):
        name = input("Enter name")
        phone = input("Enter phone")
        address = input("Enter address")
        record = Contact(name,phone,address)
        self.append(record)


ad_b = AddressBook()
luda = Contact("Luida", "0963610573", "Filatova34")
ad_b.append(luda)
print(luda)
luda.edit_contact()
print(luda)
print(ad_b)
