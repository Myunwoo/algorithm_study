def solution(number, limit, power):
    answer = 0
    arr = [0 for _ in range(number+1)]
    for n in range(1, number+1):
        for i in range(1, int((n+1)**0.5)+1):
            if n % i == 0:
                arr[n] += 1
                if i**2 != n:
                    arr[n] += 1
            if arr[n] > limit:
                arr[n] = power
                break
    return sum(arr)