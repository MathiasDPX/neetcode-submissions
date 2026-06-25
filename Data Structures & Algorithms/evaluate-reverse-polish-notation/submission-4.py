from math import ceil

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            try:
                stack.append(int(token))
                continue
            except:
                pass

            a = stack.pop()
            b = stack.pop()

            if token == '*':
                stack.append(b * a)
            elif token == '/':
                stack.append(int(b / a))
            elif token == '+':
                stack.append(b + a)
            elif token == '-':
                stack.append(b - a)
            
            print(b, token, a, '=', stack[-1])

        return stack[-1]