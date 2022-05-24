import sys

alpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

input = input()

for al in alpha:
    input = input.replace(al, 'a')
print(len(input))