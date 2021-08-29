#https://www.acmicpc.net/problem/2822
scores=[]
for i in range(8):
    scores.append([int(input()),i+1])

s=0
num=[]
scores.sort(reverse=True)
for i in range(5):
    s+=scores[i][0]
    num.append(scores[i][1])

print(s)
num.sort()
for n in num:
    print(n,end=' ')