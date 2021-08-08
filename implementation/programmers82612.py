#https://programmers.co.kr/learn/courses/30/lessons/82612
def solution(price, money, count):
    answer = -1
    s=0
    for i in range(1,count+1):
        s+=price*i
    
    if money-s < 0:
        answer=abs(money-s)
    else:
        answer=0

    return answer