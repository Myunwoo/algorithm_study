def solution(numbers, target):
    answer = 0
    
    def dfs(curIdx, total):
        nonlocal answer
        
        if curIdx == len(numbers) - 1:
            if total + numbers[curIdx] == target:
                answer += 1
            if total - numbers[curIdx] == target:
                answer += 1
            return
        
        dfs(curIdx+1, total+numbers[curIdx])
        dfs(curIdx+1, total-numbers[curIdx])
    
    dfs(0, 0)
    return answer