from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def find_block(board, f):
    empty_board_list = []
    visited = [[False] * len(board[0]) for _ in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board[i])):
            if not visited[i][j] and board[i][j] == f:
                queue = deque([(i, j)])
                board[i][j] = f ^ 1
                visited[i][j] = True
                lst = [(i, j)]

                while queue:
                    x, y = queue.popleft()
                    for _ in range(4):
                        nx, ny = x + dx[_], y + dy[_]
                        if nx < 0 or nx > len(board) - 1 or ny < 0 or ny > len(board) - 1:
                            continue
                        elif board[nx][ny] == f:
                            queue.append((nx, ny))
                            board[nx][ny] = f ^ 1
                            visited[nx][ny] = True
                            lst.append((nx, ny))
                empty_board_list.append(lst)

    return empty_board_list