import sys

T = int(sys.stdin.readline())

for _ in range(T):
    wordA, wordB = sys.stdin.readline().strip().split()
    newWordA = ''.join(sorted(list(wordA)))
    newWordB = ''.join(sorted(list(wordB)))
    if newWordA == newWordB:
        print(wordA, '&', wordB, 'are anagrams.')
    else:
        print(wordA, '&', wordB, 'are NOT anagrams.')