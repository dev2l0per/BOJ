import sys

N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    age, name = map(str, sys.stdin.readline().split())
    arr.append((int(age), name))

arr = sorted(arr, key = lambda x: (x[0]))
for val in arr:
    print(f'{val[0]} {val[1]}')