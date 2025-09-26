class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append('FizzBuzz')
            elif i % 3 == 0:
                answer.append('Fizz')
            elif i % 5 == 0:
                answer.append('Buzz')
            else:
                answer.append(str(i))
        return answer
        base = [
            "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", 
            "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"
        ]
        result = []
        for i in range(1, n+1):
            result.append(base[(i-1) % 15].replace(
                str((i-1) % 15 + 1), str(i)
            ))
        return result
