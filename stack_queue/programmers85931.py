from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    while progresses:
        count = 0
        t = (100 - progresses[0])//speeds[0]
        if (100 - progresses[0])%speeds[0] > 0:
            t += 1
        for i in range(len(progresses)):
            progresses[i] += t*speeds[i]
        while progresses:
            if progresses[0] >= 100:
                count += 1
                progresses.popleft()
                speeds.popleft()
            else:
                break
        answer.append(count)
    return answer