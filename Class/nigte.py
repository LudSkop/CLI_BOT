from collections import UserString
import re


class NumberString(UserString):
    def number_count(self):
        count = 0
        number = ""
        for element in self.data:
            if element.isdigit():
                number += element
            if not element.isdigit() and number:
                count += int(number)
                number = ""
        if number:
            count += int(number)

        return count


number = NumberString('Alisa 25, 5, 100, 12')
print(number.number_count())


# numbers = re.findall(r'\d+', self.data)  # Знайти всі числа в рядку
#         total = sum(int(num) for num in numbers)  # Підсумувати всі знайдені числа
#         return total