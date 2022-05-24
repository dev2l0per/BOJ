import sys

dp = [[0] * 501 for _ in range(501)]

n = int(sys.stdin.readline())

for i in range(1, n + 1):
    nums = list(map(int, sys.stdin.readline().split()))
    for j in range(len(nums)):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + nums[j]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + nums[j]

print(max(dp[n]))