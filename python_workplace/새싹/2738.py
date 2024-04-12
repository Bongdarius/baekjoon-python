numArr = input().split();
num1 = int(numArr[0]);
num2 = int(numArr[1]);

a = [];
b = [];

for i in range(num1):
    arr = [int(x) for x in input().split()];
    # arr = list(map(int, input().split()))
    a.append(arr);

for i in range(num1):
    arr = [int(x) for x in input().split()];
    # arr = list(map(int, input().split()))
    b.append(arr);

# for i in range(num1):
    for j in range(num2):
        a[i][j] += b[i][j];

for i in range(num1):
    mystr = "";
    for j in range(num2):
        mystr += str(a[i][j]) + " ";
    print(mystr);

# 행렬 덧셈
# result = []
# for i in range(num1):
#     row = []
#     for j in range(num2):
#         row.append(a[i][j] + b[i][j])
#     result.append(row)

# # 결과 출력
# for row in result:
#     print(*row)