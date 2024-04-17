weight = int(input())
# weight = 19
list = []
for i in range(weight // 5):
    for j in range(weight // 3):
        if(((i+1) * 5 + (j+1) * 3) == weight):
            list.append([i+1, j+1])

print(list)
# listLength = len(list)
# print(list[listLength-1])

