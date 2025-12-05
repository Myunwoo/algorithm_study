class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        newX = x
        
        arr = []
        while newX > 0:
            arr.append(newX % 10)
            newX //= 10
        
        for i in range(len(arr)//2):
            if arr[i] != arr[len(arr) - i - 1]:
                return False
        return True

# 풀이의 공간 복잡도를 개선하기 위해, 수를 뒤집어서 equal 비교하는 방식이 존재한다.
# 단, 수를 뒤집으면 수의 표현 범위를 벗어나는 일이 발생할 수 있다.
# 이떄, 수를 뒤에서 하나씩 떼어와서 길이가 같아질 때까지 이어붙이다가,
# 원본과 떼어 붙인 배열의 길이가 같아지면 비교해보는 방식도 존재한다.