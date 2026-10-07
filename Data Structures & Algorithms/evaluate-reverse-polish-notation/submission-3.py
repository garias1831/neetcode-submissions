class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = "+-*/"

        stack = []

        for t in tokens:
            # Digit case
            if t not in ops:
                stack.append(int(t))
                continue
                
            y = stack.pop()
            x = stack.pop()
            if t == '+':
                stack.append(x + y)
            elif t == '-':
                stack.append(x - y)
            elif t == '*':
                stack.append(x * y)
            elif t == '/':
                stack.append(int(x / y))

        return stack.pop()