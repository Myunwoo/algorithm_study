N = int(input())

arr = []

for _ in range(N):
    start, to, end = input().split()
    arr.append((start,end))

#시작 시간이 가장 늦은 일정
arr.sort(key=lambda x:x[0],reverse=True)
first = arr[0]

#마치는 시간이 가장 이른 일정
arr.sort(key=lambda x:x[1])
last = arr[0]

if int(first[0].replace(":","")) > int(last[1].replace(":","")):
    print(-1)
else:
    print(first[0] + " ~ " + last[1])