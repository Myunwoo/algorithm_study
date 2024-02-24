N, M = list(map(int, input().split()))
arr = list(map(int, input().split()))

for i in range(1, N):
    arr[i] += arr[i-1]

answer = []
for _ in range(M):
    i, j = list(map(int, input().split()))
    if i == 1:
        answer.append(arr[j-1])
    else:
        answer.append(arr[j-1] - arr[i-2])

for a in answer:
    print(a)