import sys
from typing import List

N: int
K: int
N, K = map(int, sys.stdin.readline().split())
inputs: List[int] = []
result: int = 0
for _ in range(N):
    inputs.append(int(sys.stdin.readline()))
for i in range(N - 1, -1, -1):
    if K >= inputs[i]:
        result += K // inputs[i]
        K = K % inputs[i]
print(result)