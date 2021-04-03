N = int(input())

matrix = []

for _ in range(N):
    matrix.append(list(input()))

def arrangement(block_size):
    global matrix
    c = 0
    for i in range(N):
        for j in range(N):
            current = matrix[i][j]
            isArranged = True
            if current == '0':
                continue
            else:
                for r in range(block_size):
                    for c in range(block_size):
                        if i+block_size >= N or j+block_size >= N:
                            isArranged = False
                            continue
                        if matrix[i+block_size][j+block_size] == '0':
                            isArranged = False
                if isArranged == True:
                    c += 1
    return c
                        

total = 0
counts = []

#가구의 크기는 1부터 공간의 크기까지
for block_size in range(1,N+1):
    count = arrangement(block_size)
    if count != 0:
        total += count
        counts.append(count)

print(total)
for count in counts:
    print(count)