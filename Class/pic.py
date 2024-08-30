import pic


def write_contacts_to_file(filename, contacts):
    with open(filename, 'wb') as file:
        pickle.dump(contacts, file)


def read_contacts_from_file(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

