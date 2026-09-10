class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = ["1"]
        idx = 2

        while idx <= n:
            if idx % 3 == 0 and idx % 5 == 0:
                answer.append("FizzBuzz")
            elif idx % 3 == 0:
                answer.append("Fizz")
            elif idx % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(idx))
            
            idx += 1
        
        return answer
            