#https://programmers.co.kr/learn/courses/30/lessons/42840
def solution(answers):
    answer = []
    num1=[1,2,3,4,5]
    num2=[2,1,2,3,2,4,2,5]
    num3=[3,3,1,1,2,2,4,4,5,5]
    count=[0,0,0]

    
    for i in range(len(answers)):
        if answers[i]==num1[i%len(num1)]:
            count[0]+=1
        if answers[i]==num2[i%len(num2)]:
            count[1]+=1
        if answers[i]==num3[i%len(num3)]:
            count[2]+=1
    m=max(count)
    for i in range(len(count)):
        if m==count[i]:
            answer.append(i+1)
    
    return answer