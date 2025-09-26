def getCost(alpha):
    cost = ord(alpha) - ord('A')
    if cost < 13:
        return cost
    else:
        return abs(26 - cost)

def solution(name):
    answer = 0
    curIdx = 0
    
    # 상/하 버튼을 눌러야 하는 횟수
    costArr = [getCost(n) for n in name]
    answer += costArr[0]
    costArr[0] = 0
    
    while sum(costArr) > 0:
        for d in range(1, len(name)):
            right = (curIdx + d) % len(name)
            left = (curIdx - d + len(name)) % len(name)
            
            if costArr[right] > 0:
                print('hwg!', right)
                answer += d
                answer += costArr[right]
                costArr[right] = 0
                curIdx = right
                break
            if costArr[left] > 0:
                print('hwg!', left)
                answer += d
                answer += costArr[left]
                costArr[left] = 0
                curIdx = left
                break
                
    
    return answer

print(solution("AABAAAAAAABBB"))