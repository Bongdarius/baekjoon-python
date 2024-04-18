#소수 찾기
#1과 자기 자신으로밖에 나누어 떨어지지 않는 수(1은 소수가 아님)

totalCnt = int(input())
list = [int(x) for x in input().split()]

# list = [1, 3, 5, 7]
list_cnt = []

for i in range(len(list)):
    list_cnt.append(0)
    for j in range(1, list[i] + 1, 1):
        if(list[i] % j == 0):
            list_cnt[i] += 1

print(list_cnt.count(2))