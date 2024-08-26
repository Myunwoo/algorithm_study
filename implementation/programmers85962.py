def solution(keymap, targets):
    answer = []
    dic = {}
    for key in keymap:
        for i in range(len(key)):
            if key[i] not in dic:
                dic[key[i]] = i+1
            elif dic[key[i]] > i+1:
                dic[key[i]] = i+1
    
    for target in targets:
        s = 0
        isGood = True
        for t in target:
            if t not in dic:
                isGood = False
                break
            s += dic[t]
            
        if isGood:
            answer.append(s)
        else:
            answer.append(-1)

    return answer