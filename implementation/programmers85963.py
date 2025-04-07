def solution(n, s):
    answer = [s//n if s//n >= 1 else 1 for _ in range(n)]
    s_answer = sum(answer)
    while s_answer < s:
        for i in range(len(answer)-1, -1, -1):
            answer[i] += 1
            s_answer += 1
            if s_answer >= s:
                break
    answer = [-1] if s_answer != s else answer
    return answer