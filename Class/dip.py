from pickle import loads, dumps


class A:
    x = 'text'
    def __init__(self):
        print('class A')
        self.y = 'нова змінна'


a = A()
s_instance = dumps(a)
s_class = dumps(A)

restored_a = loads(s_instance)
restored_A = loads(s_class)

print(a.x, a.y)
print(restored_a.x, restored_a.y)
print(a == restored_a) #False
print(A == restored_A) #True
