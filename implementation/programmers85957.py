def solution(keyinput, board):
    answer = [0, 0]
    dic = {
        'up': [0, 1],
        'down': [0, -1],
        'left': [-1, 0],
        'right': [1, 0]
    }
    hm = board[0] // 2
    vm = board[1] // 2

    for k in keyinput:
        dh, dv = dic[k]
        newH = answer[0] + dh
        newV = answer[1] + dv
        if -vm<=newV<=vm and -hm<=newH<=hm:
            answer = [newH, newV]
    
    return answer