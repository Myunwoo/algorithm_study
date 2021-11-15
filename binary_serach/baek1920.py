#https://www.acmicpc.net/problem/1920
import sys
N=int(sys.stdin.readline())
nums=list(map(int, sys.stdin.readline().strip().split()))
M=int(sys.stdin.readline())
targets=list(map(int, sys.stdin.readline().strip().split()))

nums.sort()

def binary(target):
    global N,nums,M,targets
    l=0
    r=N-1
    while l<=r:
        mid=(l+r)//2
        if nums[mid]==target:
            return 1
        elif nums[mid]<target:
            l=mid+1
        else:
            r=mid-1
    return 0
    
for target in targets:
    print(binary(target))