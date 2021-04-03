#https://www.acmicpc.net/problem/15649

N, M = map(int, input().split())

#탐색해야 할 숫자 저장 배열
nums = [i+1 for i in range(N)]
#탐색해야 할 숫자의 방문 여부
visited = [False] * N

arr = []

def dfs(depth):
    global nums
    global visited
    global arr

    if depth == M:
        print(*arr)
        return

    for i in range(N):
        if visited[i] == True:
            continue

        arr.append(nums[i])
        visited[i] = True

        dfs(depth+1)

        arr.pop()
        visited[i] = False

dfs(0)