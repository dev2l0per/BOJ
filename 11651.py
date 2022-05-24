import sys

N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    x, y = list(map(int, sys.stdin.readline().split()))
    arr.append([y, x])
arr.sort()
for val in arr:
    print(val[1], val[0])