import sys

T = int(sys.stdin.readline())

for _ in range(T):
    R, S = map(str, sys.stdin.readline().split())
    result = ""
    for char in S:
        for __ in range(int(R)):
            result += char
    print(result)