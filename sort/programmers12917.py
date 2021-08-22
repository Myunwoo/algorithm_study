def solution(s):
    answer = ''
    s=list(s)
    s.sort(reverse=True)
    for t in s:
        answer+=t
    return answer