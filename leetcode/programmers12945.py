import sys
sys.setrecursionlimit(1000000000)

def fibo(n, memo):
    if memo[n] > -1:
        return memo[n]
    
    calced = fibo(n-1, memo) + fibo(n-2, memo)
    memo[n] = calced
    return memo[n]

def solution(n):
    
    memo = [-1 for _ in range(n+1)]
    memo[0] = 0
    memo[1] = 1
    return fibo(n, memo) % 1234567