count = int(input());
arr = [];
for i in range(count):
    a = input();
    arr.append(a[0] + a[-1]);

for i in arr:
    print(i);