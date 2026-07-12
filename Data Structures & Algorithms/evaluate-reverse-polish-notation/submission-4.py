
import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ['+','-','*','/']:
                stack.append(int(token))
            else:
                if token == '+':
                    append_num = stack[-1] + stack[-2]
                    stack.pop()
                    stack.pop()
                    stack.append(append_num)
                elif token == '-':
                    append_num = stack[-2] - stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(append_num)
                elif token == '*':
                    append_num = stack[-2] * stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(append_num)
                elif token == '/':
                    append_num = math.trunc(stack[-2] / stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.append(append_num)
            print(stack)
        return stack[-1]

        