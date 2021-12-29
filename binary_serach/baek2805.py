#https://www.acmicpc.net/problem/2805
import sys
N,M=map(int, sys.stdin.readline().split())
trees=list(map(int, sys.stdin.readline().strip().split()))

def binary():
    global N,M,trees
    l=0
    r=max(trees)
    while l<=r:
        mid=(l+r)//2
        sum=0
        for tree in trees:
            if tree-mid >= 0:
                sum+=(tree-mid)
        if sum==M:
            return mid
        elif sum<M:
            r=mid-1
        else:
            l=mid+1
    return r

print(binary())