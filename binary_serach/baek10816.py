#https://www.acmicpc.net/problem/10816

N = int(input())
cards = [0 for _ in range(-10000000,10000001)]
inputs = list(map(int, input().split()))

for i in inputs:
    cards[i] += 1

M = int(input())
targets = list(map(int, input().split()))

for target in targets:
    print(cards[target], end=" ")