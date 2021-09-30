#https://www.acmicpc.net/problem/2810
#https://www.acmicpc.net/problem/2847
import sys
N=int(sys.stdin.readline())
games=[]
for _ in range(N):
    games.append(int(sys.stdin.readline()))

count=0
games.reverse()

for i in range(N-1):
    if games[i]<=games[i+1]:
        count+=games[i+1]-games[i]+1
        games[i+1]-=games[i+1]-games[i]+1

print(count)