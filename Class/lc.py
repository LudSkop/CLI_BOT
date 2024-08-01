class Contacts:
    current_id = 1


def __init__(self):
    self.contacts = []


def list_contacts(self):
    print(self.contacts)
    return self.contacts


def add_contacts(self, name, phone, email, favorite):
    dict_person = {}
    dict_person["id"] = Contacts.current_id
    dict_person["name"] = name
    dict_person["phone"] = phone
    dict_person["email"] = email
    dict_person["favorite"] = favorite
    self.contacts.append(dict_person)
    Contacts.current_id += 1

