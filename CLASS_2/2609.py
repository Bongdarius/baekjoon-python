# 최소공약수, 최소공배수
import sys

def get_divisor(x):
    if x < 1:
        return 0
    
    result_arr = [1]
    xx = int(x / 2 + 0.5)
    for i in range(2, xx + 1, 1):
        if(x % i == 0):
            result_arr.append(i)
    result_arr.append(x)
    return result_arr

def get_gcd(x_arr, y):
    for i in range(len(x_arr), 0, -1):
        x = x_arr[i - 1]
        if y % x == 0:
            return x
    return 0

def get_lcm(x, y, z):
    return int(x * y / z)
    

def solve(x, y):
    gcd = get_gcd(get_divisor(x), y)
    lcm = get_lcm(x, y, gcd)
    return [gcd, lcm]
    
input_arr = sys.stdin.readline().split()
input_arr.sort()
result_arr = solve(int(input_arr[0]), int(input_arr[1]))

for i in range(0, len(result_arr), 1):
    print(result_arr[i])
    
"""
라이브러리를 사용하는 방법
import sys
import math

x, y = map(int, sys.stdin.readline().split())

gcd = math.gcd(x, y)
lcm = math.lcm(x, y)  # Python 3.9 이상
print(gcd)
print(lcm)
"""