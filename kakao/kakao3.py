import math
def solution(fees, records):
    answer = []
    dic={}
    #출차기록 세팅
    for record in records:
        time,num,io=record.split()
        time=time.split(':')
        time=(int(time[0])*60)+int(time[1])
        if num in dic:
            dic[num].append(time)
        else:
            dic[num]=[time]
            
    results=[]
    #비용 계산
    for car in dic:
        total=0
        stack=[]
        dic[car].reverse()
        while dic[car]:
            rec=dic[car].pop()
            if stack:
                s=stack.pop()
                total+=rec-s
            else:
                stack.append(rec)
        #입차 기록만 남았을 경우
        if stack:
            s=stack.pop()
            total+=(23*60)+59-s
            
        if total <= fees[0]:
            total=fees[1]
        else:
            total=fees[1]+(math.ceil((total-fees[0])/fees[2])*fees[3])
        results.append([car,total])
    
    results.sort(key=lambda x:x[0])
    for r in results:
        answer.append(r[1])
    return answer