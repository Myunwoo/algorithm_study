def getTopKFrequentEvents(events, k):
    # print('evets', events, 'k', k)
    dic = {}
    for i in range(len(events)):
        if events[i] in dic:
            dic[events[i]][0] += 1
        else:
            dic[events[i]] = [1, i]
    
    dicList = [[dic[key][0], dic[key][1], key] for key in list(dic.keys())] 
    dicList.sort(key=lambda x: [-x[0], x[1]])
    
    # print('return', [el[2] for el in dicList[:k]])
    
    return [el[2] for el in dicList[:k]]

# 나는 이 문제 풀이에 hash, array, sort를 사용했지만,
# 만약에 evets가 chunk 단위로 들어온다? => 그럼 heap에다가 넣어서 동적으로 우선순위가 관리되도록 해야 한다.
# 왜냐? 모든 events를 한 번에 보유해놓고 sort할 수 없기 때문에