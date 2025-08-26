import sys
case = int(sys.stdin.readline())
dic = {}
for i in range(0, case, 1):
    input = int(sys.stdin.readline())
    dic[input] = dic.get(input, 0) + 1

keys = list(dic.keys())
keys.sort()

for key in keys:
    count = dic[key]
    for i in range(0, count, 1):
        print(key)