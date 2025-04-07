N = int(input())
l = list(map(int, input().split()))
maxCosts = [[0, 0, 0] for _ in range(2)]
maxCosts[1] = l
minCosts = [[0, 0, 0] for _ in range(2)]
minCosts[1] = l

for i in range(1, N):
    l = list(map(int, input().split()))
    maxCosts[0] = maxCosts[1]
    minCosts[0] = minCosts[1]
    maxCosts[1] = [0, 0, 0]
    minCosts[1] = [0, 0, 0]
    for j in range(3):
        if j == 0:
            maxCosts[1][j] = max(l[j]+maxCosts[0][j], l[j]+maxCosts[0][j+1])
            minCosts[1][j] = min(l[j]+minCosts[0][j], l[j]+minCosts[0][j+1])
        elif j == 1:
            maxCosts[1][j] = max(l[j]+maxCosts[0][j-1], l[j]+maxCosts[0][j], l[j]+maxCosts[0][j+1])
            minCosts[1][j] = min(l[j]+minCosts[0][j-1], l[j]+minCosts[0][j], l[j]+minCosts[0][j+1])
        elif j == 2:
            maxCosts[1][j] = max(l[j]+maxCosts[0][j-1], l[j]+maxCosts[0][j])
            minCosts[1][j] = min(l[j]+minCosts[0][j-1], l[j]+minCosts[0][j])

print(max(maxCosts[1]), min(minCosts[1]))