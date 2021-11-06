#https://www.acmicpc.net/problem/1461
#가장 멀리갔을때 돌아오지 않는다!!!
#가장 멀리갈때 많이 가지고 간다!!!!
N,M=map(int,input().split())
books=list(map(int, input().split()))

neg=[]
pos=[]
for book in books:
    if book<0:
        neg.append(book)
    elif book>0:
        pos.append(book)

neg.sort()
pos.sort(reverse=True)
weights=[]

for i in range(len(neg)//M):
    #한 번 이동할 때 들어야 하는 무게를 배열에 추가
    weights.append(abs(neg[i*M]))
#나누어 떨어지지 않으면 남은 것이 있다는 것
if len(neg)%M!=0:
    weights.append(abs((neg[(len(neg)//M)*M])))

for i in range(len(pos)//M):
    weights.append(pos[i*M])
if len(pos)%M!=0:
    weights.append(pos[(len(pos)//M)*M])

weights.sort()

result=weights.pop()
while weights:
    result+=2*weights.pop()
print(result)