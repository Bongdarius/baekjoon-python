# 최소공약수, 최소공배수
import sys

def get_min(x):
    if x < 1:
        return 0
    
    result_arr = [1]
    xx = int(x / 2 + 0.5)
    for i in range(2, xx + 1, 1):
        if(x % i == 0):
            result_arr.append(i)
    result_arr.append(x)
    return result_arr

def check_min(x_arr, y):
    for i in range(len(x_arr), 0, -1):
        x = x_arr[i - 1]
        if y % x == 0:
            return x
    return 0

def solve(x, y):
    return check_min(get_min(x), y)
    
input = sys.stdin.readline().split()
print(solve(int(input[0]), int(input[1])))


1, 2, 5, 10
1, 2, 3, 4, 6, 12
1, 2, 4, 5, 10, 20