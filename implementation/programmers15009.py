def solution(command):
    answer = [0, 0]
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    curDir = 0
    for c in command:
        if c == 'R':
            curDir = (curDir+1) % 4
        elif c == 'L':
            curDir -= 1
            if curDir < 0:
                curDir = 3
        elif c == 'G':
            answer[0] += direction[curDir][0]
            answer[1] += direction[curDir][1]
        elif c == 'B':
            answer[0] -= direction[curDir][0]
            answer[1] -= direction[curDir][1]
    return answer