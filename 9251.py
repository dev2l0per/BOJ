import sys
from typing import List

str1: str = sys.stdin.readline().strip()
str2: str = sys.stdin.readline().strip()

len1: int = len(str1)
len2: int = len(str2)

dp: List[List[int]] = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]

for i in range(len1 + 1):
    for j in range(len2 + 1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[-1][-1])