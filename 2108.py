import sys
from collections import Counter

N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()

print(round(sum(arr) / N))
print(arr[len(arr) // 2])

count = Counter(arr).most_common()
if len(arr) > 1:
    if count[0][1] == count[1][1]:
        print(count[1][0])
    else:
        print(count[0][0])
else:
    print(count[0][0])
print(arr[-1] - arr[0])