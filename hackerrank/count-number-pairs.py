def countAffordablePairs(prices, budget):
    if len(prices) < 2:
        return 0
    
    answer = 0
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            if prices[i] + prices[j] <= budget:
                answer += 1
    return answer

# 최초 작성한 답안 : O(n^2)



# 아래는 직접 풀지 못한 O(n) 알고리즘
def countAffordablePairs(prices, budget):
    n = len(prices)
    if n < 2:
        return 0

    left, right = 0, n - 1
    answer = 0

    while left < right:
        s = prices[left] + prices[right]

        if s <= budget:
            answer += (right - left)
            left += 1
        else:
            right -= 1

    return answer

# prices[left] + prices[right] <= budget일 경우,
# (left, left+1), (left, left+2), ... , (left, right)가 전부조건을 만족한다. 왜? prices가 오름차순임이 보장되어 있으므로.
# 따라서 prices[left] + prices[right] <= budget일 경우 answer에 right - left 추가
# prices[left] + prices[right] > budget일 경우 left를 상승시키는 것은 의미 없음. right를 감소시켜 작은 수를 만들어본다.