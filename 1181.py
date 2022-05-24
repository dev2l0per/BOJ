import sys

N = int(sys.stdin.readline())
wordSet = set()
for _ in range(N):
    wordSet.add(sys.stdin.readline().split()[0])
wordSet = sorted(wordSet, key = lambda x: (len(x), x))
for val in wordSet:
    print(val)