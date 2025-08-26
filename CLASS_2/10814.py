case = int(input())

list = []

for i in range(0, case, 1):
    age, name = map(str, input().split())
    list.append((int(age), i, name))

list.sort()

for tup in list:
    print("%d %s" %(tup[0], tup[2]))