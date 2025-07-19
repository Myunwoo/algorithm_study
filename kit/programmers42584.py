def solution(prices):
    answer = []
    
    for i in range(len(prices)):
        curPrice = prices[i]
        count = 0
        for j in range(i+1, len(prices)):
            count += 1
            if prices[j] < curPrice:
                break
        
        answer.append(count)
    
    return answer