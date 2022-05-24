import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
numSet = sorted(set(arr), key = lambda x: x)

# for O(1)
dictionary = {numSet[i] : i for i in range(len(numSet))}
for val in arr:
    print(dictionary[val], end=' ')