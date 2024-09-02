from copy import copy, deepcopy


l = [1, 2, 3, ['a', 'b', 'c']]
list_l = l[:]
l_copy = copy(l)
l_deepcopy = deepcopy(l)
print(l == list_l)
print(l == l_copy, l == l_deepcopy)
