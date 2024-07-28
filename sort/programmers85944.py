def solution(score):
    answer = []
    score = list(map(lambda x:sum(x)/2,score))
    sorted_score = sorted(score, reverse=True)
    
    for s in score:
        answer.append(sorted_score.index(s)+1)
    
    return answer