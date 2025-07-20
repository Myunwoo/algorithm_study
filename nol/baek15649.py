def backtrack(path, used):
    if len(path) == M:
        print(*path)
        return
    for i in range(1, N+1):
        if not used[i]:
            used[i] = True
            backtrack(path + [i], used)
            used[i] = False

N, M = map(int, input().split())
backtrack([], [False] * (N+1))
