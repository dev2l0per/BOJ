import sys
from typing import List

N: int = int(sys.stdin.readline())
inputs: List[int] = list(map(int, sys.stdin.readline().split()))

dp: List[int] = [1] * (N)
dp2: List[int] = [1] * (N)

for i in range(N):
    for cur in range(i):
        if inputs[i] > inputs[cur]:
            dp[i] = max(dp[i], dp[cur] + 1)

for i in range(N - 1, -1, -1):
    for cur in range(i + 1, N):
        if inputs[i] > inputs[cur]:
            dp2[i] = max(dp2[i], dp2[cur] + 1)

result: List[int] = []
for a, b in zip(dp, dp2):
    result.append(a + b)
print(max(result) - 1)