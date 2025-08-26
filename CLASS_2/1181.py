case = int(input())
_list = []
for i in range(0, case, 1):
    x = input()
    _list.append((len(x), x))
set = set(_list)
_list = list(set)
_list.sort()
    
for i in range(0, len(_list), 1):
    tup = tuple(_list[i])
    print(tup[1])