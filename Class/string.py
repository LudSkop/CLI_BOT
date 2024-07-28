from collections import UserList, UserDict


class Phones(UserList):
    def set_phone(self, phone):
        if len(phone) == 12:
            new_phone = "+" + phone
        elif len(phone) < 12:
            new_phone = "+38" + phone
        self.data.append(new_phone)

    def get_phones(self):
        return self.data


phone_list = Phones()
phone_list.set_phone('0963610573')
phone_list.set_phone('380963610573')
print(phone_list.get_phones)