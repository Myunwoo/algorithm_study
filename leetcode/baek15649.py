N, M = map(int, input().split())

def backTracking(path, used):
    if len(path) == M:
        print(*path)
        return

    for i in range(1, N+1):
        if used[i]:
            continue
        used[i] = True
        backTracking(path + [i], used)
        used[i] = False

backTracking([], [False]*(N+1))