# 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

import sys

case = int(sys.stdin.readline())
arr = []

for i in range(0, case, 1):
    x, y = map(int, sys.stdin.readline().split())
    arr.append((x, y))
    
arr.sort()
for i in arr:
    print("%d %d" %(i[0], i[1]))