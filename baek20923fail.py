#https://www.acmicpc.net/problem/20923
import sys
from collections import deque
N,M=map(int, sys.stdin.readline().split())
doDeck=deque()
doGround=deque()
suDeck=deque()
suGround=deque()

#도도의 차례, 게임이 바로 끝나는 경우, False리턴
#차례를 동시에 마치는 경우엔 즉시종료가 아니고, 결과를 비교해야 한다.
def doTurn():
    doGround.append(doDeck.pop())
    if not doDeck:
        return False
    return True


def suTurn():
    suGround.append(suDeck.pop())
    if not suDeck:
        return False
    return True

#도도가 누른 경우 True리턴
def doWin():
    if doGround:
        if doGround[len(doGround)-1]==5:
            return True
    if suGround:
        if suGround[len(suGround)-1]==5:
            return True
    return False

#수연이가 누른 경우 True리턴
def suWin():
    if not suGround and not doGround:
        if doGround[len(doGround)-1] + suGround[len(suGround)-1] == 5:
            return True
    return False

#상대방의 그라운드를 내 카드더미의 아래로
def takeCards(who):
    if who=="do":
        while suGround:
            doDeck.appendleft(suGround.pop())
    else:
        while doGround:
            suDeck.appendleft(doGround.pop())

for _ in range(N):
    d,s=map(int, sys.stdin.readline().split())
    doDeck.append(d)
    suDeck.append(s)

for _ in range(M):
    suCanWin=False
    doCanWin=False
    #도도차례
    if not doTurn():
        suCanWin=True
    #도도가 이길경우
    if doWin():
        takeCards('do')
        suCanWin=False
        continue
    #수연이가 이길경우
    if suWin():
        takeCards('su')
        continue
    #수연이 차례
    if not suTurn():
        doCanWin=True
    #도도가 이길경우
    if doWin():
        takeCards('do')
        continue
    #수연이가 이길경우
    if suWin():
        takeCards('su')
        doCanWin=False
        continue
    
    #도도, 수연이 모두 카드 없음
    if doCanWin and suCanWin:
        print('dosu')
        exit()
    elif doCanWin:
        print('do')
        exit()
    elif suCanWin:
        print('su')
        exit()



if len(suDeck)>len(doDeck):
    print('su')
elif len(suDeck)<len(doDeck):
    print('do')
else:
    print('dosu')