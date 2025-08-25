x = [int(x) for x in input().split()];
result = 0;
for i in range(5):
    x[i] *= x[i];
    result += x[i];
print(result%10);