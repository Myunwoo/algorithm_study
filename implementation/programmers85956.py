from itertools import permutations
def solution(dots):
    answer = 0
    pers = list(permutations(dots, 4))
    for a, b, c, d in pers:
        if a[1]*c[0] - b[1]*c[0] - a[1]*d[0] + b[1]*d[0] == a[0]*c[1] - b[0]*c[1] - a[0]*d[1] + b[0]*d[1]:
            answer = 1
            break
    return answer