class ListedValuesDict:
    def __init__(self):
        self.data = {}

    def __setitem__(self, key, value):
        if key in self.data:
            self.data[key].append(value)
        else:
            self.data[key] = [value]

    def __getitem__(self, key):
        result = str(self.data[key][0])
        for value in self.data[key][1:]:
            result += ", " + str(value)
        return result


l_dict = ListedValuesDict()
l_dict[1] = 'Alice'
l_dict[1] = '8'
print(l_dict[1])