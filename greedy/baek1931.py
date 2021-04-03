N = int(input())

meetings = []
a = 0
b = 0

result = []

for _ in range(N):
    a, b = map(int, input().split())
    meetings.append((a, b))

meetings.sort(key = lambda x:(x[1],x[0]))

result.append(meetings[0])

for i in range(1,len(meetings)):
    #시간표에 들어간 마지막 수업과 시간이 겹치는 수업은 건너뛰기
    if result[len(result)-1][1] > meetings[i][0]:
        continue
    else:
        result.append(meetings[i])

print(len(result))