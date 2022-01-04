#https://www.acmicpc.net/problem/15829
L=int(input())
arr=list(input())
r=31
M=1234567891

def alphToNum(alpha):
    return ord(alpha)-96

result=0
for i in range(L):
    result+=alphToNum(arr[i])*(r**i)

print(result%M)