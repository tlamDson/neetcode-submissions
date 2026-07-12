
import math
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
                    append_num = firstPop + secondPop
                    stack.append(append_num)
                elif token == '-':
                    append_num = secondPop - firstPop
                    stack.append(append_num)
                elif token == '*':
                    append_num = secondPop * firstPop
                    stack.append(append_num)
                elif token == '/':
                    append_num = math.trunc(secondPop / firstPop)
                    stack.append(append_num)
        return stack[-1]

        