def solution(id_list, report, k):
    answer = []
    c={}
    dic={}
    #중복된 신고 삭제
    report=list(set(report))
    
    for i in id_list:
        c[i]=0
        dic[i]=[]

    for r in report:
        r=r.split()
        c[r[1]]+=1
        dic[r[0]].append(r[1])
    
    for i in id_list:
        count=0
        for t in dic[i]:
            if c[t]>=k:
                count+=1
        answer.append(count)
    return answer