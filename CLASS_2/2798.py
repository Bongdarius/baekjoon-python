#블랙잭
firstInput = [int(x) for x in input().split()]

cardCount = firstInput[0]
maxNum = firstInput[1]

secondInput = [int(x) for x in input().split()]

# maxNum = 21
# secondInput = [5, 6, 7, 8, 9]

resultList = []

for x in range(0, len(secondInput), 1):
    for y in range(x + 1, len(secondInput), 1):
        # print("x = %d, y = %d" %(secondInput[x], secondInput[y]))
        for z in range(y + 1, len(secondInput), 1):
            sum = secondInput[x] + secondInput[y] + secondInput[z]
            if(sum <= maxNum):
                resultListEach = [secondInput[x],  secondInput[y],  secondInput[z]]
                # resultList.append(resultListEach)
                resultList.append(sum)
                # print("%d + %d + %d = %d" %(secondInput[x], secondInput[y], secondInput[z], sum))

resultList.sort()
print(resultList[len(resultList) - 1])