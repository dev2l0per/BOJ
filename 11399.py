import sys
from typing import List

N: int = int(sys.stdin.readline())
inputs: List[int] = list(map(int, sys.stdin.readline().split()))
inputs.sort()

for i in range(1, N):
    inputs[i] += inputs[i - 1]
print(sum(inputs))