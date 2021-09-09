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