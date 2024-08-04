class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        dict_add = {}
        dict_add['name'] = name
        dict_add['phone'] = phone
        dict_add['email'] = email
        dict_add['favorite'] = favorite
        dict_add['id'] = Contacts.curent_id
        self.contacts.append(dict_add)
        contacts.curent_id += 1


contacts = Contacts()
print(contacts.name)