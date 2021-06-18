N = int(input())

moves = list(input().split())

pos =[0,0]

for move in moves:
    if move == 'R':
        if (pos[0] + 1) >= N:
            continue
        pos[0] += 1
    elif move == 'L':
        if (pos[0] - 1) < 0:
            continue
        pos[0] -= 1
    elif move == 'U':
        if (pos[1] - 1) < 0:
            continue
        pos[1] -= 1
    
    elif move == 'D':
        if (pos[1] + 1) >= N:
            continue
        pos[1] += 1

print(str(pos[1]+1) + " " + str(pos[0]+1))