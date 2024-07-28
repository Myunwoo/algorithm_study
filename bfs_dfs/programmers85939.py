from collections import deque

def solution(numbers, target):
    answer = 0
    dq = deque()
    dq.append([0, 0])
    while dq:
        cur, curCount = dq.popleft()
        if curCount == len(numbers):
            if cur == target:
                answer += 1
            continue
        dq.append([cur+numbers[curCount], curCount+1])
        dq.append([cur-numbers[curCount], curCount+1])
    return answer