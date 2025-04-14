import sys
M, N = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().strip().split()))

start = 1
end = max(arr)
answer = 0

while start <= end:
    mid = (start + end) // 2

    count = 0
    for a in arr:
        # 현재 mid로 해당 과자를 나눌 수 있다면
        if a >= mid:
            # 몫 만큼의 과자가 만들어짐
            count += a // mid
        # 과자가 짧아서 나눌 수 없음
        else:
            continue
    
    # 나누어진 과자의 개수가 사람수보다 많아서 가능한 케이스
    if count >= M:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)