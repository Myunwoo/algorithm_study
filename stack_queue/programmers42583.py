from collections import deque

def getSum(bridge):
    s = 0
    for w, c in bridge:
        s += w
    return s

def move(bridge, bridge_length):
    temp = False
    for i in range(len(bridge)):
        bridge[i][1] += 1
        if bridge[i][1] >= bridge_length:
            temp = True
    return temp
        

def solution(bridge_length, weight, truck_weights):
    answer = 1
    tq = deque(truck_weights)
    bridge = deque()
    
    while tq:
        if getSum(bridge)+tq[0] <= weight and len(bridge) < bridge_length:
            bridge.append([tq.popleft(), 0])
        if move(bridge, bridge_length):
            bridge.popleft()
        answer += 1
    
    while bridge:
        if move(bridge, bridge_length):
            bridge.popleft()
        answer += 1
    
    return answer