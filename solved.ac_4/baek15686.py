from itertools import combinations

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

chickenArr = []
houseArr = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            houseArr.append((i, j))
        elif graph[i][j] == 2:
            chickenArr.append((i, j))

# 치킨 가게 중 M개를 선택하는 경우
combs = combinations(chickenArr, M)
result = float('inf')
for comb in combs:
    chickenTotal = 0
    # 치킨 가게 순회
    for house in houseArr:
        minLength = float('inf')
        # 가장 가까운 치킨 가게 까지의 거리
        for c in comb:
            minLength = min(minLength, abs(house[0]-c[0]) + abs(house[1]-c[1]))
        chickenTotal += minLength
    result = min(result, chickenTotal)

print(result)