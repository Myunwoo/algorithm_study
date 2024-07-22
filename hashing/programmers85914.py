def solution(s):
    answer = []
    dic = {}
    for i in range(len(s)):
        word = s[i]
        answer.append(-1 if word not in dic else i-dic[word])
        dic[word] = i
    return answer