import sys

n = int(sys.stdin.readline())

infos = []
index = 0

for _ in range(n):
    infos.append(list(sys.stdin.readline().split()))

infos.sort(key=lambda x:int(x[0]))

for info in infos:
    print(info[0] + ' ' + info[1])