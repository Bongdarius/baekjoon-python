case = int(input())
arr = []
for i in range(0, case, 1):
    x = input()
    arr.append(len(x) >= 6 and len(x) <= 9 )
for i in arr:
    if i:
        print("yes")
    else:
        print("no")