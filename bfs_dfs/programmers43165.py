def solution(numbers, target):
    answer = 0
    
    def dfs(result, i):
        nonlocal numbers
        #배열을 모두 탐색했다면, target과 일치하는지만 확인
        if i == len(numbers):
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            #result에 인덱스의 값을 더해주고 넘기는 것으로 dfs
            dfs(i+1, result+numbers[i])
            dfs(i+1, result-numbers[i])
    dfs(0,0)
    return answer