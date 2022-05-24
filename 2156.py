import sys

N = int(sys.stdin.readline())
dp = [0] * (N + 1)
liter = [0] * (N + 1)

for i in range(1, N + 1):
    liter[i] = int(sys.stdin.readline())

if N == 1:
    print(liter[1])
    sys.exit(0)
elif N == 2:
    print(liter[1] + liter[2])
    sys.exit(0)

dp[1] = liter[1]
dp[2] = liter[1] + liter[2]
dp[3] = max(liter[1] + liter[3], liter[2] + liter[3], dp[2])

for i in range(4, N + 1):
    dp[i] = max(dp[i-1], dp[i - 2] + liter[i], dp[i - 3] + liter[i - 1] + liter[i])
print(dp[N])