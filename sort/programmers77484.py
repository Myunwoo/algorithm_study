def grade(n):
    if n==6:
        return 1
    elif n==5:
        return 2
    elif n==4:
        return 3
    elif n==3:
        return 4
    elif n==2:
        return 5
    else:
        return 6

def solution(lottos, win_nums):
    answer = []
    corrects=[False for _ in range(46)]
    for win in win_nums:
        corrects[win]=True
    count=0
    pos=0
    for lotto in lottos:
        if corrects[lotto]:
            count+=1
        if lotto==0:
            pos+=1
            
    answer.append(grade(count+pos))
    answer.append(grade(count))
    
      
    return answer