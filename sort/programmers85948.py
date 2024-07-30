def solution(N, stages):
    answer = []
    done = [0 for _ in range(N+3)]
    right = [0 for _ in range(N+3)]
    
    done[1] = len(stages)
    for s in stages:
        done[s+1] -= 1
        right[s] += 1
    
    for i in range(1, N+1):
        done[i] += done[i-1]
    
    arr = [[right[i]/done[i] if done[i] != 0 else 0, i] for i in range(1, N+1)]
    arr.sort(key=lambda x:[-x[0], x[1]])
    for a in arr:
        answer.append(a[1])
    return answer