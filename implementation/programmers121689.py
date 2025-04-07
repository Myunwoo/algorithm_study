from collections import deque

def solution(menu, order, k):
    answer = 0
    orderIdx = 0
    menuDic = {}
    maxLen = 1000000
    for i in range(len(menu)):
        menuDic[i] = menu[i]
    
    waitq = deque()
    i=0
    while i<maxLen:
        if waitq:
            waitq[0] -= 1
            if waitq[0] == 0:
                waitq.popleft()
                
        if i%k == 0 and orderIdx<len(order):
            waitq.append(menu[order[orderIdx]])
            orderIdx+=1
        i+=1 
        answer = max(answer, len(waitq))
    return answer