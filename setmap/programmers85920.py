def solution(spell, dic):
    answer = 2
    for dd in dic:
        s = set(spell)
        isGood = True
        for d in dd:
            if d in s:
                s.remove(d)
            else:
                isGood = False
                break
        if isGood and len(list(s)) == 0:
            return 1
    return answer