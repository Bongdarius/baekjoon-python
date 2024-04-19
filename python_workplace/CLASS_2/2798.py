#블랙잭
firstInput = [int(x) for x in input().split()]

cardCount = firstInput[0]
maxNum = firstInput[1]

secondInput = [int(x) for x in input().split()]

for x in range(len(secondInput)):
    for y in range(len(secondInput)-1):
        for z in range(len(secondInput)-2):
            print(z)
