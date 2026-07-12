class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+': lambda a, b: a + b, '-': lambda a, b: a - b, '*': lambda a, b: a * b, '/': lambda a, b: int(a / b)}
        stack = []

        for token in tokens:
            if token in operators:
                a = stack.pop()
                b = stack.pop()
                res = operators[token](b, a)
                stack.append(res)
            else:
                stack.append(int(token))

        return stack[-1]