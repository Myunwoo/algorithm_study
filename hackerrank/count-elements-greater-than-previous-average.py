# 최초 작성한 코드
def countResponseTimeRegressions(responseTimes):
    if len(responseTimes) < 2:
        return 0
    answer = 0
    for i in range(1, len(responseTimes)):
        curAvg = sum(responseTimes[:i]) / i
        if curAvg < responseTimes[i]:
            answer += 1
    return answer

# 위 알고리즘의 시간 복잡도는 O(n^2)이다.
# responseTimes[:i] -> 이건 0번째부터 i번째까지 요소를 순회하며 새 배열을 만든다 O(n)
# sum도 순회하면 더하므로 O(n)
# 위 둘을 합쳐서 O(n) (2n이니까)
# O(n) 동작을 n만큼 루프 하므로 O(n^2)


# 두 번째 작성한 코드
def countResponseTimeRegressions(responseTimes):
    if len(responseTimes) < 2:
        return 0
    
    answer = 0
    curSum = responseTimes[0]
    for i in range(1, len(responseTimes)):
        curAvg = curSum / i
        if curAvg < responseTimes[i]:
            answer += 1
        curSum += responseTimes[i]
    
    return answer

# 세 번째 작성한 코드
def countResponseTimeRegressions(responseTimes):
    if len(responseTimes) < 2:
        return 0
    
    answer = 0
    curSum = responseTimes[0]
    for i in range(1, len(responseTimes)):
        if curSum < responseTimes[i] * i:
            answer += 1
        curSum += responseTimes[i]
    
    return answer

# if curSum < responseTimes[i] * i:
# if문에서 / 연산을 할 때 부동 소수점 문제가 발생할 수 있기 때문에
# 이런 형태로 개선해 볼 수 있다.


# 근데 사실상,
# curAvg = curSum // i 여도 상관 없다.
