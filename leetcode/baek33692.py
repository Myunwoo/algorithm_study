A, B = map(int, input().split())

answer = []
m = -1

def getHamming(i, j):
    s = 0
    one = bin(i)[2:]
    two = bin(j)[2:]

    if len(one) > len(two):
        two = '0'*(len(one) - len(two)) + two
    elif len(two) > len(one):
        one = '0'*(len(two) - len(one)) + one
    
    for i in range(len(one)):
        if one[i] != two[i]:
            s += 1
    return s

for i in range(A, B):
    for j in range(i+1, B+1):
        h = bin(i ^ j).count('1')
        if m < h:
            m = h
            answer = [i, j]


print(*answer)
