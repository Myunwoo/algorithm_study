def solution(id_pw, db):
    answer = ''
    dic = {}
    for d in db:
        dic[d[0]] = d[1]
    if id_pw[0] in dic and id_pw[1] == dic[id_pw[0]]:
        answer = 'login'
    elif id_pw[0] in dic and id_pw[1] != dic[id_pw[0]]:
        answer = 'wrong pw'
    else:
        answer = 'fail'
    return answer