def solution(rsp):
    answer = ''
    dic = {
        '2':'0',
        '0':'5',
        '5':'2'
    }
    for r in rsp:
        answer += dic[r]
    return answer