import sys

N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))
arr.sort()
for val in arr:
    print(val[0], val[1])