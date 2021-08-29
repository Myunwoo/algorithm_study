#https://www.acmicpc.net/problem/10867
N=int(input())
nums=list(map(int, input().split()))

#set을 list함수의 argument로 사용 가능
nums=list(set(nums))
nums.sort()

for n in nums:
    print(n, end=' ')