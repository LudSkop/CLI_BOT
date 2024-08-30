import pickle


data = {'Alisa': 7, 'Pusa': 4}

with open('lesson.bin', 'wb') as file:
    pickle.dump(data, file)
    


d_bytes = pickle.dumps(data)
print(d_bytes)

with open('lesson.bin', 'rb') as file:
    d_load = pickle.load(file)
    print(d_load)

d_loads = pickle.loads(d_bytes)
print(d_loads)