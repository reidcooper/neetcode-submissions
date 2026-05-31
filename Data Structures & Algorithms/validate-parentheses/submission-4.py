class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in ['[', '{', '(']:
                stack.append(c)
                continue

            if len(stack) == 0:
                return False

            top = stack[-1]

            match c:
                case '}' if top == '{':
                    stack.pop()
                case ']' if top == '[':
                    stack.pop()
                case ')' if top == '(':
                    stack.pop()
                case _:
                    return False

        return len(stack) == 0