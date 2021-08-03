#https://www.acmicpc.net/problem/10800
import sys
N=int(sys.stdin.readline())
balls=[]
for i in range(N):
    balls.append([i]+list(map(int, sys.stdin.readline().split())))
#크기 기준 balls배열 정렬
balls.sort(key=lambda x:x[2])

results=[0 for _ in range(N)]

sumOfBalls=[0 for _ in range(N)]
#첫 공은 이전에 아무 공도 더할 수 없기 때문에 0추가
total=0
results[balls[0][0]]=total
count=0

for i in range(1,N):
    #이전 공의 색과 무게
    bf_color, bf_size=balls[i-1][1]-1, balls[i-1][2]    
    #현재 공이 삼킬 수 있는 공의 무게 배열
    sumOfBalls[bf_color]+=bf_size
    #총량
    total+=bf_size

    if bf_size==balls[i][2]:
        #현재 공이 삼킬 수 있는 공의 무게를 results에 추가
        count+=1
        results[balls[i][0]]=total-sumOfBalls[balls[i][1]-1]-(bf_size*count)
    else:
        #현재 공이 삼킬 수 있는 공의 무게를 results에 추가
        results[balls[i][0]]=total-sumOfBalls[balls[i][1]-1]
        count=0

for r in results:
    print(r)