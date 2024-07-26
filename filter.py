import random


res = [random.randint(1000, 20000) for _ in range(5)]

print(res)

a = []
for _ in range(5):
    a.append(random.randint(1, 20))
print(a)

result = list(map(lambda x: x - (x * 0.02), res))
print(result)

result1 = list(map(lambda x: int(x), result))
print(result1)