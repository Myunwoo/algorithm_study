def isSmall(wallet, bill):
    return (bill[0] <= wallet[0] and bill[1] <= wallet[1]) or (bill[1] <= wallet[0] and bill[0] <= wallet[1])

def solution(wallet, bill):
    answer = 0
    while True:
        if isSmall(wallet, bill):
            break
        answer += 1
        if bill[0] > bill[1]:
            bill[0] = bill[0] // 2
        else:
            bill[1] = bill[1] // 2
        
    return answer