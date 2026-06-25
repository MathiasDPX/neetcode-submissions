class Solution:
    def isValid(self, s: str) -> bool:
        closingMap = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []

        for char in s:
            if char in [')', '}', ']']:
                if bool(stack) == False:
                    return False
                elif stack[-1] == closingMap[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not bool(stack)