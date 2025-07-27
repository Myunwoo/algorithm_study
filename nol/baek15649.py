def backTracking(path, used, M):
    if len(path) == M:
        for i in range(len(path)):
            if i == len(path) - 1:
                print(path[i]+1)
            else:
                print(path[i]+1, end=' ')
        return
    
    for i in range(N):
        if not used[i]:
            used[i] = True
            backTracking(path + [i], used, M)
            used[i] = False



N, M = map(int, input().split())
backTracking([], [False] * N, M)