ascCnt = 0
descCnt = 0

a = [int(x) for x in input().split()]
# a = [1, 2, 3, 4, 5, 6, 7, 8]
# a.reverse()

for i in range(8):
    if((i+1) == a[i]):
        ascCnt += 1
    elif((i+1) == a[7-i]):
        descCnt += 1

if(ascCnt==8):
    print("ascending")
elif(descCnt==8):
    print("descending")
else:
    print("mixed")