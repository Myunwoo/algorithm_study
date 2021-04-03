#https://www.acmicpc.net/problem/8958

T = int(input())

results = []

for _ in range(T):
    oxs = list(input())
    countO = 0
    result = 0
    for ox in oxs:
        if ox == 'O':
            countO += 1
            result += countO
        else:
            countO = 0
    
    results.append(result)

for r in results:
    print(r)