from itertools import combinations_with_replacement
N, M = map(int, input().split())

for a in combinations_with_replacement(map(str,range(1,N+1)), M):
    print(' '.join(a))