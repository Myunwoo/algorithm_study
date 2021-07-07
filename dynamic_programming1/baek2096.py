#https://www.acmicpc.net/problem/2096

n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]

large = table[0]
small = table[0]
for i in range(1, n):
    large = [max(large[0], large[1]) + table[i][0],
            max(large[0], large[1], large[2]) + table[i][1],
            max(large[1], large[2]) + table[i][2]]
    small = [min(small[0], small[1]) + table[i][0],
            min(small[0], small[1], small[2]) + table[i][1],
            min(small[1], small[2]) + table[i][2]]

print(max(large), min(small))