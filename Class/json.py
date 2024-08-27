import json


def write_contacts_to_file(filename, contacts):
    with open(filename, 'w') as file:
        result = {'contacts': contacts}
        json.dump(result, file)


def read_contacts_from_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)['contacts']

