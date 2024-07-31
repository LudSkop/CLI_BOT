from collections import UserString


class NumberString(UserString):
    def number_count(self):
        count = 0
        for element in self.data:
            if element.isdigit():
                count += int(element)
        return count


number = NumberString('Alisa 2, 5, 1,')
print(number.number_count())