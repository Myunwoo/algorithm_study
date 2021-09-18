#https://www.acmicpc.net/problem/1339
#첫 번째 트라이 - 알파벳의 등장 자릿수 * 등장 횟수 ---- 이 경우에 낮은 자리에 다수 등장하는 케이스가 오답을 만들었음
#높은 자리에 많이 등장하면서, 많이 등장하는 것이 높은 가중치를 받아야 한다!
import sys
N=int(sys.stdin.readline())
words=[]

dic={}
for _ in range(N):
    word=list(sys.stdin.readline().strip())
    words.append(word)
    #어떤 알파벳이 가장 높은 위치에 등장했을까?
    for i in range(len(word)):
        if word[i] in dic:
            dic[word[i]]+=10**(len(word)-i)
        else:
            dic[word[i]]=10**(len(word)-i)

#자릿수 기반 정렬
arr=[]
for d in dic:
    arr.append([d,dic[d]])
arr.sort(key=lambda x:x[1])

#자릿수를 가중치로 변환
cost=9
dic={}
while arr:
    a=arr.pop()
    dic[a[0]]=cost
    cost-=1

#합계
answer=0
for word in words:
    temp=''
    for w in word:
        temp+=str(dic[w])
    answer+=int(temp)

print(answer)