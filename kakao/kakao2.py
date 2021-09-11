def isPrimeNum(n):
    if n==1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def solution(n, k):
    answer = 0
    t=[]
    while n!=0:
        t.append(n%k)
        n=n//k
    t.reverse()
    num=''
    for i in t:
        num+=str(i)
    num=num.split('0')
    for n in num:
        if n=='':
            continue
        if isPrimeNum(int(n)):
            answer+=1
    
    return answer