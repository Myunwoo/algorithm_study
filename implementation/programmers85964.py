def dateToNum(date):
    y, m, d = map(int, date.split('.'))
    return y*12*28 + m*28 + d

def solution(today, terms, privacies):
    answer = []
    today = dateToNum(today)
    dic = {}
    for term in terms:
        t, v = term.split()
        dic[t] = int(v)*28
    
    for i in range(len(privacies)):
        date, t = privacies[i].split()
        date = dateToNum(date) + dic[t]
        if date <= today:
            answer.append(i+1)
    return answer