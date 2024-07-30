from collections import UserList, UserDict


class Phones(UserList):
    def set_phone(self, phone):
        if len(phone) == 12:
            new_phone = "+" + phone
        elif len(phone) < 12:
            new_phone = "+38" + phone
        else:
            raise
        self.data.append(new_phone)

    def get_phones(self):
        return self.data


#phone_list = Phones()
#phone_list.set_phone('0963610573')
#phone_list.set_phone('380963610573')
#print(phone_list.get_phones)


class User(UserDict):
    def set_name(self, name):
        self.data['name'] = name

    def get_name(self):
        return self.data.get('name')

    def set_phone(self, phone):
        phone_list = self.data.get('phones', Phones())
        phone_list.data.append(phone)
        self.data['phones'] = phone_list

    def get_phones(self):
        return self.data.get('phones')


user_1 = User()
user_1.set_name('Alisa')
user_1.set_phone('380983864330')
user_1.set_phone('0963610573')
user_1.set_phone('380637362574')
print(user_1.get_phones())
print(user_1.get_name(), user_1.get_phones())



