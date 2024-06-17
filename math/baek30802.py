N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

t = 0
for size in sizes:
    t += size // T + (1 if size % T > 0 else 0)

print(t)
print(N // P, N % P)