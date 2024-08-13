def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            l = -1 if j-1 < 0 else triangle[i-1][j-1]
            r = -1 if j+1 > len(triangle[i-1]) else triangle[i-1][j]
            triangle[i][j] += max(l, r)
    return max(triangle[-1])