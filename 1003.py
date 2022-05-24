import sys

dp = [
    [1, 0],
    [0, 1],
]

for i in range(2, 41):
    dp.append([dp[i - 1][0] + dp[i - 2][0], dp[i - 1][1] + dp[i - 2][1]])

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    print(f'{dp[N][0]} {dp[N][1]}')