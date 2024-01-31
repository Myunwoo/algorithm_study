import sys
input = sys.stdin.readline

fibo = [[1, 0], [0, 1]]

for i in range(2, 41):
    fibo.append([fibo[i-2][0]+fibo[i-1][0], fibo[i-2][1]+fibo[i-1][1]])

T = int(input())
answer = []
for _ in range(T):
    N = int(input())
    answer.append(fibo[N])

for a in answer:
    print(a[0], a[1])