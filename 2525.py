import sys

h, m = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())

m += c
while m >= 60:
    h += 1
    m -= 60
if h >= 24:
    h -= 24
print(f'{h} {m}')