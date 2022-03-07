def solution(numbers, target):
    count=0
    def dfs(pre, index):
        #이전까지의 총합에 현재 인덱스의 수를 더하고, 빼기
        l=pre+numbers[index]
        r=pre-numbers[index]
        #끝에 다다른 경우
        if index==len(numbers)-1:
            nonlocal count
            if l==target:
                count+=1
            if r==target:
                count+=1
            return
        dfs(l,index+1)
        dfs(r,index+1) 
    dfs(0,0)
        
    return count