N, M = map(int, input().split())

cards = []

for _ in range(N):
    temp = list(map(int, input().split()))
    temp.sort()
    cards.append(temp[0])

cards.sort(reverse=True)

print(cards[0])