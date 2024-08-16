def solution(board):
    answer = 0
    dn = [-1, -1, -1, 0, 0, 1, 1, 1]
    dm = [-1, 0, 1, -1, 1, -1, 0, 1]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                for k in range(8):
                    newN = i + dn[k]
                    newM = j + dm[k]
                    if 0<=newN<len(board) and 0<=newM<len(board[0]) and board[newN][newM] == 0:
                        board[newN][newM] = 2
            
    
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                answer += 1
                
    return answer