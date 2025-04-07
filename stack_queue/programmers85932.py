from collections import deque

def solution(priorities, location):
    answer = 0
    dq = deque()
    for i in range(len(priorities)):
        dq.append([priorities[i], i])
    while True:
        cur = dq.popleft()
        exe = True
        for d in dq:
            if d[0] > cur[0]:
                dq.append(cur)
                exe = False
                break
        if not exe:
            continue
        answer += 1
        if cur[1] == location:
            break
    return answer