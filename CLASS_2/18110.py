import sys
case = int(sys.stdin.readline())
if case == 0:
    print(0)
else:
    x = int(case * 0.15 + 0.5)
    arr = []
    for i in range(0, case, 1):
        arr.append(int(sys.stdin.readline()))
    arr.sort()
    arr = arr[x: case - x: 1]
    print(int(sum(arr) / len(arr) + 0.5))