class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        slovar = {")": "(", "]": "[", "}": "{"}
        for i in s:
            if i in "({[":
                stack.append(i)
            elif stack and stack[-1] == slovar[i]:
                stack.pop()
            else:
                return False
        return not stack