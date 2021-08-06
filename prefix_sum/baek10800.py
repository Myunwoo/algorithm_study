#https://www.acmicpc.net/problem/10800
import sys
N=int(sys.stdin.readline())
balls=[]
for i in range(N):
    balls.append([i]+list(map(int, sys.stdin.readline().split())))
#크기 기준 balls배열 정렬
balls.sort(key=lambda x:x[2])

sumOfBalls=[0 for _ in range(N)]
total=0
j=0
for i in range(N):
    cur=balls[i]
    #과거의 공들 중 현재보다 가벼운 것들의 무게를 누적
    while balls[j][2] < balls[i][2]:
        total+=balls[j][2]
        sumOfBalls[balls[j][1]-1]+=balls[j][2]
        j+=1
    #총 무게 - 현재 공의 색깔의 누적합을 balls에 추가
    balls[i].append(total-sumOfBalls[cur[1]-1])


balls.sort(key=lambda x:x[0])

for b in balls:
    print(b[3])