import json


data = {
    'developer': {
        'name': 'Людмила',
        'test': 'програміст',
    }
}

with open('test.json', 'w') as file:
    json.dump(data, file)

with open('test.json', 'r') as file:
    res = json.load(file)
    print(res)


with open('text.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False)

with open('text.json', mode='r', encoding='utf-8') as file:
    result = json.load(file)
    print(result)


def write_json(name, data, mode='w', encoding='utf-8', ensure_ascii=True,):
    with open(f'{name}.json', mode=mode, encoding=encoding,) as file:
        json.dump(data, file, ensure_ascii=ensure_ascii)


def read_json(name, mode='r', encoding='utf-8'):
    with open(name, mode=mode, encoding=encoding)as file:
        result = json.load(file)
        print(result)


