#https://www.acmicpc.net/problem/9095

import sys

T = int(sys.stdin.readline().strip())

arr = [-1 for _ in range(11)]
results = []

arr[0] = 0
arr[1] = 1
arr[2] = 2
arr[3] = 4

def dpSum(num):
    global arr
    if arr[num] == -1:
        arr[num] = dpSum(num-1) + dpSum(num-2) + dpSum(num-3)
        return arr[num]
    else:
        return arr[num]


for _ in range(T):
    results.append(dpSum(int(sys.stdin.readline().strip())))

for result in results:
    print(result)