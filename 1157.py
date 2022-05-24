import sys

word = input()
word = word.upper()

cnt = [0] * 26

for char in word:
    cnt[ord(char) - ord('A')] += 1

maxCnt = max(cnt)
if cnt.count(maxCnt) > 1:
    print('?')
else:
    print(chr(cnt.index(maxCnt) + ord('A')))