def solution(lottos, win_nums):
    answer = []
    m = 0
    n = 0
    dic = {
        6:1,
        5:2,
        4:3,
        3:4,
        2:5,
        1:6,
        0:6
    }
    for l in lottos:
        if l == 0:
            m += 1
        elif l in win_nums:
            n += 1
    answer = [dic[n+m], dic[n]]
    return answer