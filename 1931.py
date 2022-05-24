import sys
from typing import List, Tuple

N: int = int(sys.stdin.readline())
inputs: List[List] = []

for _ in range(N):
    inputs.append(list(map(int, sys.stdin.readline().split())))
inputs.sort(key = lambda x: (x[1], x[0]))
endTime: int = inputs[0][1]
result: int = 1
for i in range(1, N):
    if inputs[i][0] >= endTime:
        endTime = inputs[i][1]
        result += 1
print(result)