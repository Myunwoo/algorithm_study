def solution(answers):
    answer = []
    result = [0, 0, 0]
    
    ansOne = [1, 2, 3, 4, 5]
    ansTwo = [2, 1, 2, 3, 2, 4, 2, 5]
    ansThree = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        if answers[i] == ansOne[i % len(ansOne)]:
            result[0] += 1
        if answers[i] == ansTwo[i % len(ansTwo)]:
            result[1] += 1
        if answers[i] == ansThree[i % len(ansThree)]:
            result[2] += 1
    
    m = max(result)
    for i in range(len(result)):
        if result[i] == m:
            answer.append(i+1)
    
    return answer