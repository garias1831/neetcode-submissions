class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) == 0: return True
        if len(s) % 2 != 0: return False

        opening = {'[', '{', '('}        
        closing = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        stack = []

        for c in s:
            if c in opening:
                stack.append(c)
            else:
                if len(stack) == 0 or closing[c] != stack[-1]:
                    return False
                stack.pop()
        
        return len(stack) == 0
            

        