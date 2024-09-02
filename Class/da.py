from copy import copy, deepcopy


l = [1, 2, 3, ['a', 'b', 'c']]
list_l = l[:]
l_copy = copy(l)
l_deepcopy = deepcopy(l)
print(l == list_l)
print(l == l_copy, l == l_deepcopy)

l[0] = 9
print(l, list_l, l_copy, l_deepcopy)

l[3][0] = 'Hello'
print(l, list_l, l_copy, l_deepcopy)
