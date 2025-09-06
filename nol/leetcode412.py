class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
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