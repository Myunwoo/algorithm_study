import sys
N,M=map(int, sys.stdin.readline().split())
trees=list(map(int, sys.stdin.readline().strip().split()))

l, r = 0, max(trees)
goal = r

# 이분탐색의 시간 복잡도는 O(logN)이다.
# N의 최대가 1000000, M의 최대가 2000000000 이므로,
# 1,000,000 * log2,000,000,000 = 9백만 정도.
while l <= r:
    mid = (r+l) // 2
    s = 0
    for tree in trees:
        if tree-mid > 0:
            s+=tree-mid

    if s==M:
        goal = mid
        break
    elif s<M:
        r = mid-1
        goal = r
    elif s>M:
        l = mid+1

print(goal)