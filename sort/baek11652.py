#https://www.acmicpc.net/problem/11652
import sys
from collections import Counter
N=int(sys.stdin.readline())
cards=[]
for _ in range(N):
    cards.append(int(sys.stdin.readline()))

cards=Counter(cards).most_common()
########Counter.most_common()을 활용해도 꼭 정렬이 되어있음이 보장되진 않는구나...?
cards.sort(key=lambda x:[-x[1],x[0]])

print(cards[0][0])

#####딕셔너리를 활용한 풀이
n = int(input())
dic = {}

for case in range(n):
    tmp = int(input())
    if tmp in dic:
        dic[tmp] += 1
    else:
        dic[tmp] = 1

dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
print(dic)
print(dic[0][0])