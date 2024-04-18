list = []
while(True):
    tempList = [int(x) for x in input().split()]
    tempList.sort()

    if(not tempList[0] and not tempList[0] and not tempList[0]):
        break

    if(tempList[0] ** 2 + tempList[1] ** 2 == tempList[2] ** 2):
        list.append("right")
    else:
        list.append("wrong")

for i in list:
    print(i)

