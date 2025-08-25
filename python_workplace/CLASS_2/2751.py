import sys

case = int(sys.stdin.readline())
arr = []
for i in range(0, case, 1):
    arr.append(int(sys.stdin.readline()))
arr.sort()

for i in range(0, len(arr), 1):
    print(arr[i])