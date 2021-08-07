#https://programmers.co.kr/learn/courses/30/lessons/42586
def solution(progresses, speeds):
    answer = []
    progresses.reverse()
    speeds.reverse()
    
    while progresses:
        count = 0
        p = progresses.pop()
        s = speeds.pop()
        
        if (100 - p) % s == 0:
            days = (100 - p) // s
        else:
            days = (100 - p) // s + 1
        count += 1
        
        while True:
            if progresses and progresses[len(progresses)-1] + (speeds[len(speeds)-1] * days) >= 100:
                count += 1
                progresses.pop()
                speeds.pop()
            else:
                break
        
        answer.append(count)
    
    return answer