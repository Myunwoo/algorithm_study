#https://www.acmicpc.net/problem/9461

T = int(input())

#P = [0,1,1,1,2,2,3,4,5,7,9]
P = [-1 for _ in range(101)]
P[1] = 1
P[2] = 1
P[3] = 1
P[4] = 2
P[5] = 2
P[6] = 3
P[7] = 4
P[8] = 5
P[9] = 7
P[10] = 9

def wave(num):
    if num <= 5:
        return P[num]
    else:
        if P[num] == -1:
            P[num] = wave(num-1) + wave(num-5)
        return P[num]


Ns = []

for _ in range(T):
    Ns.append(int(input()))

for n in Ns:
    print(wave(n))