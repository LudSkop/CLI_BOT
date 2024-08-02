class IDException(Exception):
    pass


def add_id(id_list, employee_id):
    if employee_id.startswith('01'):
        id_list.append(employee_id)
        return id_list
    raise IDException


my_id_list = []
try:
    print(add_id(my_id_list, '0105'))
    print(add_id(my_id_list, '0156'))
except IDException:
    print(f"Помилка: ID не починається з '01'")


print(my_id_list)