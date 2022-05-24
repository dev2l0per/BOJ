import sys
from typing import List

N: int = int(sys.stdin.readline())
inputs: List[int] = list(map(int, sys.stdin.readline().split()))

sortedInputs: List[int] = sorted(list(set(inputs)))
M: int = len(sortedInputs)
dp: List[int] = [[-1 for _ in range(M + 1)] for _ in range(N + 1)]

for i in range(N + 1):
    for j in range(M + 1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif inputs[i-1] == sortedInputs[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])