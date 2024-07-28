def solution(score):
    answer = []
    score = list(map(lambda x:sum(x)/2,score))
    sorted_score = sorted(score, reverse=True)
    
    for s in score:
        # index로 최초일치를 가져오므로, 공동 등수 처리 가능
        answer.append(sorted_score.index(s)+1)
    
    return answer