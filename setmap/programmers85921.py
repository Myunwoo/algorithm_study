def solution(my_string):
    answer = ''
    s = set()
    for m in my_string:
        if m not in s:
            answer += m
            s.add(m)
    return answer