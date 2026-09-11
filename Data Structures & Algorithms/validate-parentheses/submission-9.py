class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        data = {')':'(','}':'{',']':'['}
        for bracket in s:
            if bracket in data.values():
                stack.append(bracket)
            elif stack and data[bracket] in stack[-1]:
                stack.pop()
            else:
                return False
        return not stack




        