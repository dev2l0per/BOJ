import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
operators = list(map(int, sys.stdin.readline().split()))
arr = []

def backtrack(num, plus, minus, multiply, divide, depth):
    if depth == N:
        arr.append(num)
    if plus > 0:
        backtrack(num + A[depth], plus - 1, minus, multiply, divide, depth + 1)
    if minus > 0:
        backtrack(num - A[depth], plus, minus - 1, multiply, divide, depth + 1)
    if multiply > 0:
        backtrack(num * A[depth], plus, minus, multiply - 1, divide, depth + 1)
    if divide > 0:
        backtrack(int(num / A[depth]), plus, minus, multiply, divide - 1, depth + 1)

backtrack(A[0], operators[0], operators[1], operators[2], operators[3], 1)
print(max(arr))
print(min(arr))