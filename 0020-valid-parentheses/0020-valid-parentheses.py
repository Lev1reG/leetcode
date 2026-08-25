class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket == '(' or bracket == '{' or bracket == '[':
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                lastBracket = stack.pop()
                if lastBracket == '(' and bracket != ')':
                    return False
                elif lastBracket == '{' and bracket != '}':
                    return False
                elif lastBracket == '[' and bracket != ']':
                    return False
        return len(stack) == 0
