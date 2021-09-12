#https://www.acmicpc.net/problem/13164
N,K=map(int, input().split())
students=list(map(int, input().split()))
diff=[]
for i in range(len(students)-1):
    diff.append(students[i+1]-students[i])

diff.sort(reverse=True)
answer=0
for _ in range(N-K):
    answer+=diff.pop()

print(answer)