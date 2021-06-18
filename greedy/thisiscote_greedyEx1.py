N, M, K = map(int, input().split())

numbers = list(map(int, input().split()))

numbers.sort(reverse=True)

result = 0

first = numbers[0]
second = numbers[1]

while True:
    for _ in range(K):
        if M == 0:
            break
        result += first
        M -= 1
    if M == 0:
        break
    result += second
    M -= 1



print(result)