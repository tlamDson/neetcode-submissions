class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ['+','-','*','/']:
                stack.append(int(token))
            else:
                firstPop = stack.pop()
                secondPop = stack.pop()
                if token == '+':
                    stack.append(firstPop + secondPop)
                elif token == '-':
                    stack.append(secondPop - firstPop)
                elif token == '*':
                    stack.append(secondPop * firstPop)
                elif token == '/':
                    stack.append(int(secondPop / firstPop))
        return stack[-1]

        