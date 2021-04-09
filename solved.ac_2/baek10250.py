#https://www.acmicpc.net/problem/10250

import sys

T = int(sys.stdin.readline().strip())
results = []

for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().strip().split())
    room_num = ((N-1) // H) + 1
    if room_num < 10:
        room_num = '0' + str(room_num)
    else:
        room_num = str(room_num)

    floor_num = N % H
    if floor_num == 0:
        floor_num = H
    floor_num = str(floor_num)
    results.append(floor_num+room_num)

for result in results:
    print(result)