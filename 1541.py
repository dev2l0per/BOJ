import sys
from typing import List

inputs: List[str] = sys.stdin.readline().split('-')
result: int = 0

for input in inputs[0].split('+'):
    result += int(input)

for input in inputs[1:]:
    for num in input.split('+'):
        result -= int(num)
print(result)