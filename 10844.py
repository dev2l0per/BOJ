# 0 1 1 1 1 1 1 1 1 1
# 1 1 2 2 2 2 2 2 2 1
# 1 3 3 4 4 4 4 4 3 2

import sys

MOD = 1000000000
N = int(sys.stdin.readline())

dp = [[0] * 10 for _ in range(101)]

for i in range(1, 10):
    dp[1][i] = 1
for i in range(2, N + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][j + 1]
        elif j == 9:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
print(sum(dp[N]) % MOD)