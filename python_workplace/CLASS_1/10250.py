caseCnt = int(input())
caseList = []
resultList = []
for i in range(caseCnt):
    caseList.append([int(x) for x in input().split()])

for i in range(caseCnt):
    h = caseList[i][0]
    w = caseList[i][1]
    c = caseList[i][2]
    list_ = []

    for i in range(h):
        list_.append([])
        for j in range(w):
            list_[i].append(str(i+1) + str(j+1).zfill(2))

    list__ = []

    for j in range(w):
        for i in range(h):
            list__.append(list_[i][j])

    print(list__[c - 1])