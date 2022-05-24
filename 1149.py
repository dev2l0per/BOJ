import sys

dp = [[0] * 3 for _ in range(1001)]

N = int(sys.stdin.readline())

for i in range(1, N + 1):
    R, G, B = map(int, sys.stdin.readline().split())
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + R
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + G
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + B

print(min(dp[N]))