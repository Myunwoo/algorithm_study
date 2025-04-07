def solution(X, Y):
    answer = ''
    count = [[0, 0] for _ in range(10)]
    arr = []
    for x in X:
        count[int(x)][0] += 1
    for y in Y:
        count[int(y)][1] += 1
    
    for i in range(10):
        m = min(count[i][0], count[i][1])
        for _ in range(m):
            arr.append(str(i))
    
    arr.sort(reverse=True)
    if len(arr) == 0:
        answer = '-1'
    elif arr[0] == '0' and arr[-1] == '0':
        answer = '0'
    else:
        answer = ''.join(arr)
    
    return answer