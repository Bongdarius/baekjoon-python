#분해합
inputVal = int(input())
result = 0
for i in range(1, inputVal + 1, 1):
    eachSum = sum(map(int, str(i)))

    if(i + eachSum == inputVal):
        result = i
        break
print(result)