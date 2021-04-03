#https://www.acmicpc.net/problem/17298

N = int(input())
As = list(map(int, input().split()))

results = []

def NGE(index):
    global As
    target = As[index]
    for i in range(index+1,N):
        if As[i] > target:
            results.append(As[i])
            return
    results.append(-1)

for i in range(len(As)):
    NGE(i)

for result in results:
    print(result, end=" ")