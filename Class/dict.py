class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Owner:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def info(self):
        return {
            'name': self.name,
            'age': self.age,
            'address': self.address
        }


class Dog(Animal):
    def __init__(self, nickname, weight, breed, ):
        self.breed = breed
        self.owner = None

        super().__init__(nickname, weight)

    def say(self):
        return "Woof"

    def who_is_owner(self,):
        if self.owner:
            return self.owner.info()
        return 'no owner'


dog = Dog('Barsik', 10, 'labrador')
print(dog.nickname, dog.weight, dog.breed)
owner = Owner('Oleg', 51, 'filatova 34')
print(owner.name, owner.age, owner.address)
dog.owner = owner
print(dog.who_is_owner())

