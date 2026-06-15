class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {']':'[', '}':'{', ')':'('}
        stack = []
        
        for i in s:
            if i in '[({':
                stack.append(i)
            elif i in ')]}' and stack and bracket_dict[i] == stack[-1]:
                stack.pop()
            else:
                return False
        return len(stack) == 0