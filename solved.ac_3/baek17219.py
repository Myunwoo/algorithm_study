import sys
input = sys.stdin.readline

dic = {}
N, M = list(map(int, input().split()))
for _ in range(N):
  addr , pw = input().strip().split()
  dic[addr] = pw

for _ in range(M):
  addr = input().strip()
  print(dic[addr])