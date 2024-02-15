import sys
import deque
input = sys.stdin.readline

N, M = list(map(int, input().split()))
graph = [list(input().rstrip()) for _ in range(N)]
costs = [[0 for _ in range(M)] for _ in range(N)]

