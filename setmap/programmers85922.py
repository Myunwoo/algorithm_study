from collections import Counter

def solution(array):
    answer = 0
    c = Counter(array).most_common()
    if len(c) > 1 and c[0][1] == c[1][1]:
        answer = -1
    else:
        answer = c[0][0]
    return answer