import sys
from typing import List

N: int = int(sys.stdin.readline())
inputs: List[int] = list(map(int, sys.stdin.readline().split()))

dp: List[int] = [0 for _ in range(N)]

dp[0] = inputs[0]
for i in range(1, N):
    dp[i] = max(dp[i - 1] + inputs[i], inputs[i])
print(max(dp))