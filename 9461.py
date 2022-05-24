# 1 1 1 2 2 3 4 5 7 9 12 16 21
import sys

dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2

for i in range(6, 101):
    dp[i] = dp[i - 1] + dp[i - 5]

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    print(dp[N])