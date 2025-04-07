import copy

def solution(park, routes):
    answer = []
    dic = {
        'E': [0, 1],
        'W': [0, -1],
        'N': [-1, 0],
        'S': [1, 0]
    }
    cur = []
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                cur = [i, j]
    
    for route in routes:
        new = copy.deepcopy(cur)
        isGood = True
        direction, count = route.split(' ')
        count = int(count)
        d = dic[direction]
        
        for _ in range(count):
            new[0] += d[0]
            new[1] += d[1]
            if 0>new[0] or new[0]>=len(park) or 0>new[1] or new[1]>=len(park[0]) or park[new[0]][new[1]] == 'X':
                isGood = False
                break
        if isGood:
            cur = copy.deepcopy(new)
    answer = cur
    return answer