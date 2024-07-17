def solution(answers):
    answer = []
    n1, n2, n3 = 0, 0, 0
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [2, 1, 2, 3, 2, 4, 2, 5]
    arr3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if arr1[i % len(arr1)] == answers[i]:
            n1 += 1
        if arr2[i % len(arr2)] == answers[i]:
            n2 += 1
        if arr3[i % len(arr3)] == answers[i]:
            n3 += 1
    m = max(n1, n2, n3)
    temp = [n1, n2, n3]
    for i in range(3):
        if temp[i] == m:
            answer.append(i+1)
    return answer