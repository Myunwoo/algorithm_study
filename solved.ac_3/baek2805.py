import sys
input = sys.stdin.readline

N, M = list(map(int, input().rstrip().split()))
heights = list(map(int, input().rstrip().split()))
heights.sort()

start, end = 1, 2000000000
