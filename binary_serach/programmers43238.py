def solution(n, times):
    answer = 0
    
    # left = 최소 시간
    # right = 모든 사람이 최악의 심사관에게 심사받을 때의 시간
    left, right = 1, n*times[len(times)-1]
    
    while left<right:
        # 이분 탐색을 위한 중간값
        # mid 시간만큼 모든 심사관이 심사했을 때, 몇 명의 사람을 심사할 수 있는지 구한다.
        mid = (left+right)//2 + 1
        count = 0
        for t in times:
            count += mid//t
            # 계산 도중, count가 n을 넘어가면 더 계산할 필요 없이 right를 당겨야 하므로 탈출
            if count >= n:
                break
        if count >= n:
            answer = mid
            right = mid-1
        else:
            left = mid
    
    return answer