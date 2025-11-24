class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = ['0' for _ in range(n)]
        for i in range(1, n+1):
            value = ''
            if i % 3 == 0 and i % 5 == 0:
                value = 'FizzBuzz'
            elif i % 3 == 0:
                value = 'Fizz'
            elif i % 5 == 0:
                value = 'Buzz'
            else:
                value = str(i)
            answer[i-1] = value
        return answer
    
# 이 답변의 시간 복잡도는 O(N)이라고 하기 쉬움. 그러나,
# str(i)가 잡아먹는 시간 까지를 따지자면 O(NlogN)이다.
# python의 str 함수는 숫자를 반복적으로 10으로 나누는 연산이
# 발생하기 때문에 O(logN)으로 따질 수 있음).