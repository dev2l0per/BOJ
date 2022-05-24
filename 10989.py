import sys

N = int(sys.stdin.readline())
arr = [0] * 10001

for _ in range(N):
    num = int(sys.stdin.readline())
    arr[num] += 1

for i in range(len(arr)):
    for j in range(arr[i]):
        print(i)
