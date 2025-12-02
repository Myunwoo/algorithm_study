def mergeHighDefinitionIntervals(intervals):
    intervals.sort(key=lambda x: [x[0], x[1]])
    
    if len(intervals) < 2:
        return intervals
    
    idx = 1
    answer = [intervals[0]]
    while idx < len(intervals):
        answer[-1]
        intervals[idx]
        
        if intervals[idx][0] <= answer[-1][1]:
            answer[-1] = [min(answer[-1][0], intervals[idx][0]), max(answer[-1][1], intervals[idx][1])]
        else:
            answer.append(intervals[idx])
        idx += 1
    return answer

# 이 문제 풀때마다 느끼는거지만 항상 최초에 정렬 순서를 intervals.sort(key=lambda x: [x[1], x[0]]) 이렇게 잡는다.
# [0, 0] [1, 1] [0, 2]가 있다고 할 때 문제의 의도대로라면 하나가 되어야 하지만, 나의 정렬 순서를 따르면 하나가 될 수 없다.
# 그리고, 겹치는 부분 찾는건데 형광펜 그어서 겹치는 부분 찾는거 생각해봐라.
# 시작점이 작은 것부터 시작해서 죽죽 긋고 겹치는거 찾는게 맞잖아.
