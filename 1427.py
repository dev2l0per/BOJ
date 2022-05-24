import sys

input = input()
arr = []
for val in input:
    arr.append(val)
arr.sort(reverse=True)
for val in arr:
    print(val, end='')