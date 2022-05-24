import sys

N = int(sys.stdin.readline())
nums = list(input())
result = 0

for i in range(N):
    result += int(nums[i])

print(result)