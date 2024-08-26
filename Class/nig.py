import pickle


class Human:
    def __init__(self, name):
        self.name = name


bob = Human("Bob")
encoded_bob = pickle.dumps(bob)

decoded_bob = pickle.loads(encoded_bob)

bob.name == decoded_bob.name