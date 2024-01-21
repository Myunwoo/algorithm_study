N = int(input())
scores = list(map(int, input().split()))

m = max(scores)
scores = [score/m*100 for score in scores]
print(sum(scores)/N)