# 이항계수를 구하는 문제
import math
import sys

n, k = map(int, sys.stdin.readline().split())
print(math.comb(n, k))