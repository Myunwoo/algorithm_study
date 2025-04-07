def solution(id_list, report, k):
    answer = []
    doDic = {}
    didDic = {}
    for rep in report:
        a, b = rep.split(' ')
        # 신고 하기 dic
        if a in doDic:
            doDic[a].add(b)
        else:
            doDic[a] = set()
            doDic[a].add(b)
        # 신고 받기 dic
        if b in didDic:
            didDic[b].add(a)
        else:
            didDic[b] = set()
            didDic[b].add(a)
    for i in id_list:
        if i not in doDic:
            answer.append(0)
        else:
            curSet = doDic[i]
            s = 0
            for cur in curSet:
                if cur in didDic and len(didDic[cur]) >= k:
                    s += 1
            answer.append(s)
        
    return answer