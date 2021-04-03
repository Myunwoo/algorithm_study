#https://www.acmicpc.net/problem/2675

T = int(input())

results = []

for i in range(T):
    R, S = input().split()
    R = int(R)
    S = list(S)

    results.append(list())

    for s in S:
        for _ in range(R):
            results[i].append(s)

for result in results:
    for r in result:
        print(r,end="")
    print()