import sys

N = int(sys.stdin.readline())
cnt = 0

for _ in range(N):
    word = input()
    checkList = []
    for i in range(len(word)):
        if i != len(word) -1 and word[i] == word[i + 1]:
            continue
        if word[i] not in checkList:
            checkList.append(word[i])
        else:
            cnt += 1
            break
print(N - cnt)