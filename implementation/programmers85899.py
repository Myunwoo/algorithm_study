def solution(num, total):
    answer = []
    arr = [i for i in range(-1000, 1001)]
    for i in range(2001-num):
        if sum(arr[i:i+num]) == total:
            answer = arr[i:i+num]
    return answer