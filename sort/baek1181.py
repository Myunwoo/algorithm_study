import sys

n = int(sys.stdin.readline())

words = []

for _ in range(n):
    word = str(sys.stdin.readline())
    words.append((word,len(word)))

words = list(set(words))

words.sort(key=lambda x:(x[1],x[0]))

for word in words:
    print(word[0],end='')