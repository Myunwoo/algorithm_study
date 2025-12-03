def findNextGreaterElementsWithDistance(readings):
    answer = [[-1, -1] for _ in range(len(readings))]
    stack = []
    
    for i in range(len(readings)):
        read = readings[i]
        if not stack or read <= stack[-1][0]:
            stack.append([read, i])
            continue

        
        while stack and stack[-1][0] < read:
            cur = stack.pop()
            answer[cur[1]] = [read, i - cur[1]]
        stack.append([read, i])
        
    
    return answer