def solution(survey, choices):
    answer = ''
    dic = {
        'R': 0,
        'T': 0,
        'C': 0,
        'F': 0,
        'J': 0,
        'M': 0,
        'A': 0,
        'N': 0
    }
    
    for i in range(len(survey)):
        c = choices[i]
        s = survey[i]
        if c == 1:
            dic[s[0]] += 3
        elif c == 2:
            dic[s[0]] += 2
        elif c == 3:
            dic[s[0]] += 1
        elif c == 5:
            dic[s[1]] += 1
        elif c == 6:
            dic[s[1]] += 2
        elif c == 7:
            dic[s[1]] += 3

    if dic['R'] < dic['T']:
        answer += 'T'
    else:
        answer += 'R'
    if dic['C'] < dic['F']:
        answer += 'F'
    else:
        answer += 'C'
    if dic['J'] < dic['M']:
        answer += 'M'
    else:
        answer += 'J'
    if dic['A'] < dic['N']:
        answer += 'N'
    else:
        answer += 'A'
    return answer

